CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE "user" (
	"name" varchar NOT NULL,
	email varchar NOT NULL,
	phone varchar NOT NULL,
	unit varchar NOT NULL,
	street varchar NOT NULL,
	city varchar NOT NULL,
	state varchar NOT NULL,
	country varchar NOT NULL,
	postal varchar NOT NULL,
	id uuid NOT NULL DEFAULT uuid_generate_v4()
);

CREATE TABLE property (
	id uuid NOT NULL DEFAULT uuid_generate_v4(),
	unit varchar NULL,
	street varchar NOT NULL,
	city varchar NOT NULL,
	state varchar NOT NULL,
	postal varchar NOT NULL,
	country varchar NOT NULL,
	property_value int4 NOT NULL,
	existing_mortgage int4 NOT NULL
);

CREATE TABLE event (
	"timestamp" timestamp NOT NULL,
	email varchar NOT NULL,
	"type" varchar NOT NULL,
	message varchar NOT NULL
);

CREATE OR REPLACE VIEW public.metrics
AS WITH total_applied AS (
         SELECT 'Total Users Applied'::text AS metric,
            to_char(e."timestamp", 'YYYY-MM'::text) AS date,
            count(u.id) AS count
           FROM "user" u
             JOIN event e ON u.email::text = e.email::text
          WHERE e.message::text ~~ '%applied%'::text
          GROUP BY (to_char(e."timestamp", 'YYYY-MM'::text))
          ORDER BY (to_char(e."timestamp", 'YYYY-MM'::text))
        ), total_rejected AS (
         SELECT 'Total Users Rejected'::text AS metric,
            to_char(e."timestamp", 'YYYY-MM'::text) AS date,
            count(u.id) AS count
           FROM "user" u
             JOIN event e ON u.email::text = e.email::text
          WHERE e.message::text ~~ '%reject%'::text
          GROUP BY (to_char(e."timestamp", 'YYYY-MM'::text))
          ORDER BY (to_char(e."timestamp", 'YYYY-MM'::text))
        ), total_paid_off_50 AS (
         SELECT 'Total Users Paid off 50% of their mortgage'::text AS metric,
            NULL::text AS date,
            count(u.id) AS count
           FROM "user" u
             JOIN property p ON NULLIF(u.unit::text, ''::text)::integer = NULLIF(p.unit::text, ''::text)::double precision::integer AND lower(u.street::text) = lower(p.street::text) AND u.state::text = p.state::text
          WHERE ((p.property_value::numeric - p.existing_mortgage::numeric) / p.property_value::numeric * 100::numeric)::integer >= 50
        )
 SELECT total_applied.metric,
    total_applied.date,
    total_applied.count
   FROM total_applied
UNION ALL
 SELECT total_rejected.metric,
    total_rejected.date,
    total_rejected.count
   FROM total_rejected
UNION ALL
 SELECT total_paid_off_50.metric,
    total_paid_off_50.date,
    total_paid_off_50.count
   FROM total_paid_off_50;