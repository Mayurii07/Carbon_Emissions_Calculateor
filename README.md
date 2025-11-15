# 🌱 Carbon Emission Calculator

**DBMS Mini Project | Python + SQLite**

A comprehensive desktop application for tracking, analyzing, and reducing carbon emissions from various daily activities. This system calculates carbon footprints based on transportation, energy consumption, waste management, and industrial activities, providing users with detailed reports and personalized recommendations.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange.svg)
![SQLite](https://img.shields.io/badge/SQLite-Database-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🚀 Features

### Core Functionality
- **Multi-Tab Interface**: Query Database, Insert Data, and Carbon Reports tabs
- **Real-time Calculations**: Automatic carbon emission calculations using emission factors
- **Data Visualization**: Interactive charts and graphs using Matplotlib
- **Comprehensive Reporting**: Summary, charts, and detailed data views
- **User Management**: Profile creation and management
- **Carbon Offset Tracking**: Monitor carbon reduction activities

### Emission Tracking Categories
- **Transportation**: Car, Bus, Train, Airplane, Bicycle, Electric vehicles
- **Energy Consumption**: Electricity, Natural Gas, Solar, Wind, Coal
- **Waste Management**: Plastic, Paper, Glass, Metal, Organic waste
- **Industrial Activities**: Manufacturing, Construction, Chemical processing
- **Carbon Offsets**: Tree planting, Renewable energy credits, Methane capture

### Advanced Features
- **Predefined SQL Queries**: 50+ ready-to-use database queries
- **Custom Query Interface**: Execute custom SQL queries with syntax highlighting
- **Data Export**: Export reports and query results
- **Query History**: Navigate through previously executed queries
- **Date Range Filtering**: Analyze emissions over specific time periods
- **Personalized Recommendations**: AI-powered suggestions for emission reduction

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|----------|------------|---------|
| **Frontend** | Python Tkinter | Desktop GUI interface |
| **Backend** | Python 3.7+ | Application logic and calculations |
| **Database** | SQLite | Data storage and management |
| **Data Analysis** | Pandas | Data manipulation and analysis |
| **Visualization** | Matplotlib | Charts and graphs |
| **Date Handling** | datetime | Date operations and formatting |

### Dependencies
```
tkinter (built-in with Python)
sqlite3 (built-in with Python)
pandas
matplotlib
```

---

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/carbon-emission-calculator.git
   cd carbon-emission-calculator
   ```

2. **Install dependencies**
   ```bash
   pip install pandas matplotlib
   ```

3. **Run the application**
   ```bash
   python carbon_emission_app.py
   ```

### First-Time Setup
The application will automatically:
- Create the SQLite database (`carbon_emission.db`)
- Set up all required tables
- Insert sample data for demonstration
- Launch the GUI interface

---

## 🎯 Usage

### Getting Started

1. **Launch the Application**
   ```bash
   python carbon_emission_app.py
   ```

2. **Database Setup**
   - The database is automatically created on first run
   - Sample data is pre-loaded for testing

### Main Interface Tabs

#### 1. Query Database Tab
- **Custom Queries**: Write and execute your own SQL queries
- **Predefined Queries**: Choose from 50+ built-in queries
- **Query History**: Navigate previous queries
- **Results Display**: View data in tabular format

#### 2. Insert Data Tab
- **User Profile**: Add new users
- **Transportation**: Record travel activities
- **Energy Consumption**: Log energy usage
- **Waste Management**: Track waste generation
- **Industrial Activity**: Monitor industrial emissions
- **Carbon Offset**: Record offset activities

#### 3. Carbon Reports Tab
- **Summary View**: Overview of emissions by category
- **Charts**: Visual representation with pie charts and bar graphs
- **Details**: Detailed tables of all activities
- **Recommendations**: Personalized reduction suggestions

### Example Workflow

1. **Create User Profile**
   - Go to "Insert Data" tab
   - Select "User Profile" category
   - Enter name, email, and location

2. **Record Activities**
   - Add transportation data (vehicle type, distance)
   - Log energy consumption (source, kWh)
   - Track waste generation (type, weight)

3. **Generate Reports**
   - Select user in "Carbon Reports" tab
   - Set date range
   - Click "Generate Report"
   - View summary, charts, and recommendations

---

## 🗄️ Database Schema

### Core Tables

#### User_Profile
```sql
CREATE TABLE User_Profile (
    User_ID INTEGER PRIMARY KEY,
    Full_Name VARCHAR(100),
    Email VARCHAR(100),
    Location VARCHAR(100)
);
```

#### Transportation
```sql
CREATE TABLE Transportation (
    Transport_ID INTEGER PRIMARY KEY,
    User_ID INTEGER,
    Vehicle_Type VARCHAR(50),
    Distance_KM FLOAT,
    Date DATE,
    FOREIGN KEY (User_ID) REFERENCES User_Profile(User_ID)
);
```

#### Energy_Consumption
```sql
CREATE TABLE Energy_Consumption (
    Energy_ID INTEGER PRIMARY KEY,
    User_ID INTEGER,
    Energy_Source VARCHAR(50),
    Consumption_KWH FLOAT,
    Date DATE,
    FOREIGN KEY (User_ID) REFERENCES User_Profile(User_ID)
);
```

#### Waste_Management
```sql
CREATE TABLE Waste_Management (
    Waste_ID INTEGER PRIMARY KEY,
    User_ID INTEGER,
    Waste_Type VARCHAR(50),
    Waste_Weight_KG FLOAT,
    Date DATE,
    FOREIGN KEY (User_ID) REFERENCES User_Profile(User_ID)
);
```

#### Industrial_Activity
```sql
CREATE TABLE Industrial_Activity (
    Industry_ID INTEGER PRIMARY KEY,
    User_ID INTEGER,
    Activity_Type VARCHAR(100),
    Emission_Produced FLOAT,
    Date DATE,
    FOREIGN KEY (User_ID) REFERENCES User_Profile(User_ID)
);
```

#### Emission_Factor
```sql
CREATE TABLE Emission_Factor (
    Factor_ID INTEGER PRIMARY KEY,
    Source_Type VARCHAR(50),
    Emission_Per_Unit FLOAT
);
```

#### Carbon_Offset
```sql
CREATE TABLE Carbon_Offset (
    Offset_ID INTEGER PRIMARY KEY,
    User_ID INTEGER,
    Offset_Type VARCHAR(50),
    Offset_Amount FLOAT,
    Date DATE,
    FOREIGN KEY (User_ID) REFERENCES User_Profile(User_ID)
);
```

### Relationships
- User_Profile → Transportation (1:M)
- User_Profile → Energy_Consumption (1:M)
- User_Profile → Waste_Management (1:M)
- User_Profile → Industrial_Activity (1:M)
- User_Profile → Carbon_Offset (1:M)
- Transportation → Emission_Factor (M:1)
- Energy_Consumption → Emission_Factor (M:1)
- Waste_Management → Emission_Factor (M:1)

---

## 📁 Project Structure

```
carbon-emission-calculator/
│
├── carbon_emission_app.py      # Main application GUI
├── carbon_emission_db.py       # Database setup and schema
├── data_insertion.py           # Data insertion forms
├── reports.py                  # Reports and visualization
├── predefined_queries.py       # Basic SQL queries
├── updated_queries.py          # Advanced SQL queries
│
├── README.md                   # Project documentation
├── USER_MANUAL.docx           # Detailed user guide
├── DBMS_REPORT_FINAL.docx     # Project report
├── Carbon Emission Calculator.md  # Project overview
│
├── carbon_emission.db         # SQLite database (auto-generated)
│
└── requirements.txt           # Python dependencies
```

### Key Files Description

- **`carbon_emission_app.py`**: Main application with Tkinter GUI
- **`carbon_emission_db.py`**: Database creation and sample data insertion
- **`reports.py`**: Report generation with Matplotlib charts
- **`data_insertion.py`**: Dynamic forms for data entry
- **`predefined_queries.py`**: Collection of useful SQL queries
- **`updated_queries.py`**: Advanced queries with CTEs and window functions

---

## 🔍 Sample Queries

### Basic Queries
```sql
-- View all users
SELECT * FROM User_Profile;

-- Total emissions by user
SELECT up.User_ID, up.Full_Name, SUM(er.Emission_Amount) as Total_Emissions
FROM User_Profile up
LEFT JOIN Emission_Record er ON er.Source_ID = up.User_ID
GROUP BY up.User_ID;
```

### Advanced Queries
```sql
-- Carbon footprint view
SELECT up.User_ID, up.Full_Name,
       COALESCE(SUM(t.Distance_KM * ef_t.Emission_Per_Unit), 0) as Transport_Emissions,
       COALESCE(SUM(ec.Consumption_KWH * ef_e.Emission_Per_Unit), 0) as Energy_Emissions,
       COALESCE(SUM(co.Offset_Amount), 0) as Carbon_Offset
FROM User_Profile up
LEFT JOIN Transportation t ON up.User_ID = t.User_ID
LEFT JOIN Emission_Factor ef_t ON t.Vehicle_Type = ef_t.Source_Type
LEFT JOIN Energy_Consumption ec ON up.User_ID = ec.User_ID
LEFT JOIN Emission_Factor ef_e ON ec.Energy_Source = ef_e.Source_Type
LEFT JOIN Carbon_Offset co ON up.User_ID = co.User_ID
GROUP BY up.User_ID;
```

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to functions
- Test database operations thoroughly
- Update documentation for new features

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Project Guide**: Prof. Sachin Bhandari Sir
- **Institution**: NMIMS Mukesh Patel School of Technology Management & Engineering, Shirpur
- **Student**: Mayuri Pawar (70022300258)

---

## 📞 Support

For questions or support:
- Check the [USER_MANUAL.docx](USER_MANUAL.docx) for detailed instructions
- Review the [DBMS_REPORT_FINAL.docx](DBMS_REPORT_FINAL.docx) for technical details
- Open an issue on GitHub

---

**Made with ❤️ for a greener future**
