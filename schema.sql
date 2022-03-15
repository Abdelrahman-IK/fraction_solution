CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE public.users (
	"name" varchar NOT NULL,
	email varchar NOT NULL,
	phone varchar NOT NULL,
	street varchar NOT NULL,
	city varchar NOT NULL,
	state varchar(2) NOT NULL,
	country varchar NOT NULL,
	postal varchar NOT NULL,
	id uuid NOT NULL DEFAULT uuid_generate_v4()
);

CREATE TABLE property (
	id uuid NOT NULL DEFAULT uuid_generate_v4(),
	unit varchar NULL,
	street varchar NOT NULL,
	city varchar NOT NULL,
	state varchar(2) NOT NULL,
	postal varchar NOT NULL,
	country varchar NOT NULL,
	property_value int4 NOT NULL,
	existing_mortgage int4 NOT NULL
);

CREATE TABLE events (
	"timestamp" timestamp NOT NULL,
	email varchar NOT NULL,
	"type" varchar NOT NULL,
	message varchar NOT NULL
);
