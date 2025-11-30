CREATE TABLE Apartment (
    id SERIAL PRIMARY KEY,
    owner VARCHAR(100) NOT NULL,
    street VARCHAR(100), 
    n_of_house INT,
    n_of_apartment INT
);

CREATE TABLE chore_type (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    is_have_counter BOOL NOT NULL,
    cost_per_month numeric(10, 2)
);

CREATE TABLE payment (
    id SERIAL PRIMARY KEY,
    chore_id INT REFERENCES chore_type(id) ON DELETE CASCADE,
    apartment_id INT REFERENCES apartment(id) ON DELETE CASCADE,
    cost NUMERIC(15, 2),
    month_year VARCHAR(100),
    date_of_deposit DATE NOT NULL
);
