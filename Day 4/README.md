## ETL Project Progress

### Data Extraction

* Extracted the Customer 360 dataset from Kaggle.
* Loaded the available CSV files separately using Pandas.
* Extracted the main datasets: Customers, Orders, and Products.

### Data Profiling

* Performed profiling before data transformation.
* Analyzed dataset dimensions, columns, data types, missing values, duplicate records, unique values, and statistical information.
* Identified potential data-quality issues for further processing.

### Data Preprocessing

* Checked and handled duplicate customer records using `customer_id`.
* Checked and handled duplicate product records using `product_id`.
* Converted `order_date` into the appropriate datetime format.
* Checked missing and invalid values before integration.

### Data Transformation

* Standardized date values and data types.
* Created surrogate keys for dimension tables.
* Created a Date Dimension with `date_key` and date attributes.
* Prepared the order data for the fact table.
* Mapped business keys to warehouse surrogate keys.

### Data Integration

* Integrated customer, product, order, and date information using the available business keys.
* Used `customer_id` and `product_id` to connect orders with their respective dimensions.
* Mapped `order_date` to the Date Dimension using `date_key`.

### Data Warehouse

Created a Star Schema consisting of:

**Dimension Tables**

* `dim_customer`
* `dim_product`
* `dim_date`

**Fact Table**

* `fact_orders`

The `fact_orders` table contains:
`order_id`, `customer_key`, `product_key`, `date_key`, `quantity`, `price`, and `total_amount`.

### Data Validation

* Checked duplicate and null keys.
* Validated customer, product, and date foreign keys.
* Checked referential integrity.
* Checked negative quantities, prices, and total amounts.
* Compared `total_amount` with `quantity × price` to identify possible inconsistencies.

### Data Warehouse Export

The final warehouse tables were exported as CSV files:

* `dim_customer.csv`
* `dim_product.csv`
* `dim_date.csv`
* `fact_orders.csv`

The exported data is ready for further database loading, analysis, and visualization.
