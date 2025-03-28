/* OJO: Para correr el archivo añade esta opción:
    mysql -u root --default-character-set=utf8 calendarioapec < calendario.sql
Sin el --default-character-set, no se van a guardar los acentos adecuadamente! */

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100),
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

/* It's not stock status. It's meant to label deprecated or upcoming products for instance.*/
CREATE TABLE AvailabilityStatus (
    availability_id INT AUTO_INCREMENT PRIMARY KEY,
    status VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Brands (
    brand_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    brand_name varchar(100) NOT NULL
);

CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    sku VARCHAR(100) NOT NULL UNIQUE,
    types JSON NOT NULL,
    availability_id INT NOT NULL,
    description TEXT,
    image varchar(200),
    price DECIMAL(10, 2) NOT NULL,
    brand_id INT,
    stock INT,

    FOREIGN KEY (availability_id) REFERENCES AvailabilityStatus(availability_id),
    FOREIGN KEY (brand_id) REFERENCES Brands(brand_id)
);

CREATE TABLE OrderStatus (
    order_status_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE ShippingTypes (
    shipping__type_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    shipping_cost DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    invoice_required TINYINT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2),
    order_status_id INT NOT NULL,
    shipping_type INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (order_status_id) REFERENCES OrderStatus(order_status_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

/*Any change on OrderDetails, needs to update updated_at in Orders*/
CREATE TABLE OrderDetails (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE InvoiceDetails (
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    order_id INT NOT NULL,
    rfc CHAR(13) NOT NULL,
    address VARCHAR(200),
    email VARCHAR(100),
    razon_social VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE
);
