# Dairy Flow Backend

Welcome to the Dairy Flow backend-api repository! Dairy Flow is a management solution tailored for milk shops, offering features like record keeping, batch addition of milk on a daily basis, bookkeeping, and monthly accounts.

## Features

- **Customer Management:** Efficiently manage customer records.
- **Supplier Management:** Manage supplier records.
- **Record Keeping:** Efficiently manage inventory records for different types of milk products.
- **Delivery:** Maintain Delivery record for each customer on a daily-basis.
- **Bookkeeping:** Keep track of transactions, sales, and purchases for accurate bookkeeping.
- **Bill Generation:** Generate Monthly Bills on demand with ease.
- **Monthly Accounts:** Generate monthly reports and accounts to analyze business performance.

## Tech Stack

- **Framework:** Flask
- **Database:** MongoDB

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python 3.10.12
- MongoDB

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mohammadryanchahour/dairy-flow-backend-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd dairy-flow-backend-api
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up MongoDB:

   - Install MongoDB according to your operating system instructions.
   - Start MongoDB service.

5. Configure the application:

   - Create a `.env` file in the project root directory from .env.example.

   ```bash
   cp .env.example .env
   ```

6. Run the application:

   ```bash
   python app.py
   ```

   or

   ```bash
   python3 app.py
   ```

Now, you should be able to access the Dairy Flow backend-api locally at `http://localhost:3000`.
