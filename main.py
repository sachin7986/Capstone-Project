import pandas as pd
import matplotlib.pyplot as plt
import os

# Create folders if they don't exist
for folder in ['visualizations', 'report']:
    if not os.path.exists(folder):
        os.makedirs(folder)

def complete_analysis():
    print("🚀 Initializing Full Data Pipeline...")
    
    # 1. Load & Clean Data
    try:
        df = pd.read_csv('data/sales_data.csv')
        df['Date'] = pd.to_datetime(df['Date']) # Convert to date format
        print("✅ Data loaded and date formats standardized.")
    except Exception as e:
        print(f"❌ Error: {e}")
        return

    # 2. Key Metrics Analysis
    total_rev = df['Total_Sales'].sum()
    top_prod = df.groupby('Product')['Total_Sales'].sum().idxmax()
    
    # 3. Visualizations
    print("📊 Generating Visualizations...")
    
    # Chart 1: Bar Chart (Sales by Product)
    plt.figure(figsize=(10,6))
    df.groupby('Product')['Total_Sales'].sum().sort_values().plot(kind='barh', color='teal')
    plt.title('Total Revenue by Product Category')
    plt.xlabel('Revenue (₹)')
    plt.tight_layout()
    plt.savefig('visualizations/sales_by_product.png')

    # Chart 2: Pie Chart (Sales by Region)
    plt.figure(figsize=(8,8))
    df.groupby('Region')['Total_Sales'].sum().plot(kind='pie', autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
    plt.title('Regional Sales Contribution')
    plt.ylabel('')
    plt.savefig('visualizations/sales_by_region.png')
# --- New Section: Generate the Text Report ---
    report_path = 'report/analysis_report.md'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# 📊 Week 4: E-commerce Performance Report\n\n")
        f.write(f"## 🔍 Executive Summary\n")
        f.write(f"This automated report summarizes the analysis of {len(df)} transactions.\n\n")
        f.write(f"## 📈 Key Business Metrics\n")
        f.write(f"- **Total Revenue:** ₹{total_rev:,.2f}\n")
        f.write(f"- **Top Performing Product:** {top_prod}\n")
        f.write(f"- **Data Source:** data/sales_data.csv\n\n")
        f.write(f"## 💡 Business Insights\n")
        f.write(f"1. **Revenue Leader:** The '{top_prod}' category is driving the majority of income.\n")
        f.write(f"2. **Market Reach:** Sales are distributed across all regions, showing a healthy market presence.\n")
        
    print(f"✅ Report successfully generated at: {report_path}")
    print("✅ Analysis complete. Files saved in 'visualizations/' and 'report/' folders.")

if __name__ == "__main__":
    complete_analysis()