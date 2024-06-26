{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Invoice ID</th>\n",
       "      <th>Branch</th>\n",
       "      <th>City</th>\n",
       "      <th>Customer type</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Product line</th>\n",
       "      <th>Unit price</th>\n",
       "      <th>Quantity</th>\n",
       "      <th>Tax 5%</th>\n",
       "      <th>Total</th>\n",
       "      <th>Date</th>\n",
       "      <th>Time</th>\n",
       "      <th>Payment</th>\n",
       "      <th>cogs</th>\n",
       "      <th>gross margin percentage</th>\n",
       "      <th>gross income</th>\n",
       "      <th>Rating</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>750-67-8428</td>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>Member</td>\n",
       "      <td>Female</td>\n",
       "      <td>Health and beauty</td>\n",
       "      <td>74.69</td>\n",
       "      <td>7</td>\n",
       "      <td>26.1415</td>\n",
       "      <td>548.9715</td>\n",
       "      <td>1/5/2019</td>\n",
       "      <td>13:08</td>\n",
       "      <td>Ewallet</td>\n",
       "      <td>522.83</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>26.1415</td>\n",
       "      <td>9.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>226-31-3081</td>\n",
       "      <td>C</td>\n",
       "      <td>Naypyitaw</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Female</td>\n",
       "      <td>Electronic accessories</td>\n",
       "      <td>15.28</td>\n",
       "      <td>5</td>\n",
       "      <td>3.8200</td>\n",
       "      <td>80.2200</td>\n",
       "      <td>3/8/2019</td>\n",
       "      <td>10:29</td>\n",
       "      <td>Cash</td>\n",
       "      <td>76.40</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>3.8200</td>\n",
       "      <td>9.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>631-41-3108</td>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Male</td>\n",
       "      <td>Home and lifestyle</td>\n",
       "      <td>46.33</td>\n",
       "      <td>7</td>\n",
       "      <td>16.2155</td>\n",
       "      <td>340.5255</td>\n",
       "      <td>3/3/2019</td>\n",
       "      <td>13:23</td>\n",
       "      <td>Credit card</td>\n",
       "      <td>324.31</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>16.2155</td>\n",
       "      <td>7.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>123-19-1176</td>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>Member</td>\n",
       "      <td>Male</td>\n",
       "      <td>Health and beauty</td>\n",
       "      <td>58.22</td>\n",
       "      <td>8</td>\n",
       "      <td>23.2880</td>\n",
       "      <td>489.0480</td>\n",
       "      <td>1/27/2019</td>\n",
       "      <td>20:33</td>\n",
       "      <td>Ewallet</td>\n",
       "      <td>465.76</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>23.2880</td>\n",
       "      <td>8.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>373-73-7910</td>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Male</td>\n",
       "      <td>Sports and travel</td>\n",
       "      <td>86.31</td>\n",
       "      <td>7</td>\n",
       "      <td>30.2085</td>\n",
       "      <td>634.3785</td>\n",
       "      <td>2/8/2019</td>\n",
       "      <td>10:37</td>\n",
       "      <td>Ewallet</td>\n",
       "      <td>604.17</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>30.2085</td>\n",
       "      <td>5.3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Invoice ID Branch       City Customer type  Gender  \\\n",
       "0  750-67-8428      A     Yangon        Member  Female   \n",
       "1  226-31-3081      C  Naypyitaw        Normal  Female   \n",
       "2  631-41-3108      A     Yangon        Normal    Male   \n",
       "3  123-19-1176      A     Yangon        Member    Male   \n",
       "4  373-73-7910      A     Yangon        Normal    Male   \n",
       "\n",
       "             Product line  Unit price  Quantity   Tax 5%     Total       Date  \\\n",
       "0       Health and beauty       74.69         7  26.1415  548.9715   1/5/2019   \n",
       "1  Electronic accessories       15.28         5   3.8200   80.2200   3/8/2019   \n",
       "2      Home and lifestyle       46.33         7  16.2155  340.5255   3/3/2019   \n",
       "3       Health and beauty       58.22         8  23.2880  489.0480  1/27/2019   \n",
       "4       Sports and travel       86.31         7  30.2085  634.3785   2/8/2019   \n",
       "\n",
       "    Time      Payment    cogs  gross margin percentage  gross income  Rating  \n",
       "0  13:08      Ewallet  522.83                 4.761905       26.1415     9.1  \n",
       "1  10:29         Cash   76.40                 4.761905        3.8200     9.6  \n",
       "2  13:23  Credit card  324.31                 4.761905       16.2155     7.4  \n",
       "3  20:33      Ewallet  465.76                 4.761905       23.2880     8.4  \n",
       "4  10:37      Ewallet  604.17                 4.761905       30.2085     5.3  "
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv('supermarket_sales.csv')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Yangon', 'Naypyitaw', 'Mandalay'], dtype=object)"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['City'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Health and beauty', 'Electronic accessories',\n",
       "       'Home and lifestyle', 'Sports and travel', 'Food and beverages',\n",
       "       'Fashion accessories'], dtype=object)"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Product line'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import plotly.express as px\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Load the data\n",
    "df = pd.read_csv('supermarket_sales.csv')\n",
    "\n",
    "#Web Page configuration\n",
    "st.set_page_config(page_title='Supermarket Dashboard',\n",
    "                   page_icon ='',\n",
    "                   initial_sidebar_state='expanded',\n",
    "                   )\n",
    "\n",
    "#The layout\n",
    "hero = st.container()\n",
    "topRow = st.container()\n",
    "midRow = st.container()\n",
    "chartRow = st.container()\n",
    "footer = st.container()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Edit the sidebar\n",
    "with st.sidebar:\n",
    "    st.markdown(f'''\n",
    "            <style>\n",
    "            section[data-testid='stSidebar']{{\n",
    "                    width:500px;\n",
    "                    background-color: white;\n",
    "                    }}\n",
    "            section[data-testid='stSidebar'] h1 {{\n",
    "                   color: black;\n",
    "                    }}\n",
    "            section[data-testid='stSidebar'] p {{\n",
    "                   color: black;\n",
    "                   text-align:left;\n",
    "                   }}\n",
    "            section[data-testid='stSidebar'] svg {{\n",
    "                   fill: #ddd;\n",
    "                   }}\n",
    "            </style>\n",
    "        ''', unsafe_allow_html=True)\n",
    "    st.title(':anchor: About the dataset')\n",
    "    st.markdown(\"The growth of supermarkets in most populated cities are increasing and market competitions are also high. In this dashboard we'll give it a try and turn everything into a readable visualizations.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "#The Selectbox\n",
    "Product_lines = df['Product line'].unique()\n",
    "line = st.selectbox(' ',['Choose the product line']+list(Product_lines))\n",
    "if line == 'Choose the product line':\n",
    "    chosen_line = df\n",
    "else:\n",
    "    chosen_line = df[df['Product line'] == line]\n",
    "    \n",
    "#Customizing the select box\n",
    "st.markdown(f'''\n",
    "        <style>\n",
    "            .stSelectbox div div {{\n",
    "                background-color: #fafafa;\n",
    "                color: #333;\n",
    "            }}\n",
    "            .stSelectbox div div:hover{{\n",
    "                cursor: pointer\n",
    "            }}\n",
    "            .stSelectbox div div .option{{\n",
    "                background-color:red;\n",
    "                color: #111\n",
    "            }}\n",
    "            .stSelectbox div div svg{{\n",
    "                fill: black;\n",
    "            }}\n",
    "        </style>\n",
    "        ''', unsafe_allow_html=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1000 entries, 0 to 999\n",
      "Data columns (total 17 columns):\n",
      " #   Column                   Non-Null Count  Dtype  \n",
      "---  ------                   --------------  -----  \n",
      " 0   Invoice ID               1000 non-null   object \n",
      " 1   Branch                   1000 non-null   object \n",
      " 2   City                     1000 non-null   object \n",
      " 3   Customer type            1000 non-null   object \n",
      " 4   Gender                   1000 non-null   object \n",
      " 5   Product line             1000 non-null   object \n",
      " 6   Unit price               1000 non-null   float64\n",
      " 7   Quantity                 1000 non-null   int64  \n",
      " 8   Tax 5%                   1000 non-null   float64\n",
      " 9   Total                    1000 non-null   float64\n",
      " 10  Date                     1000 non-null   object \n",
      " 11  Time                     1000 non-null   object \n",
      " 12  Payment                  1000 non-null   object \n",
      " 13  cogs                     1000 non-null   float64\n",
      " 14  gross margin percentage  1000 non-null   float64\n",
      " 15  gross income             1000 non-null   float64\n",
      " 16  Rating                   1000 non-null   float64\n",
      "dtypes: float64(7), int64(1), object(9)\n",
      "memory usage: 132.9+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [],
   "source": [
    "# The Hero Section\n",
    "with hero:\n",
    "    # the logo\n",
    "    st.markdown(\"\"\"<div style=\"position:relative; margin: auto; text-align: center;\">\n",
    "              <img src=\"https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Map-circle-blue.svg/1024px-Map-circle-blue.svg.png\" width=56>\n",
    "            </div>\"\"\", unsafe_allow_html=True)\n",
    "\n",
    "    # the header\n",
    "    st.markdown('<h1 style=\"text-align:center; position:relative; top:40%;\">Super Store DATA</h1>', unsafe_allow_html=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [],
   "source": [
    "# The Rows\n",
    "with topRow:\n",
    "\n",
    "    # Calculate the total number of invoices\n",
    "    total_invoices = chosen_line.shape[0]\n",
    "\n",
    "    # Calculate the average rating and number of ratings\n",
    "    average_rating = chosen_line['Rating'].mean()\n",
    "\n",
    "    # Find the most active time for invoices\n",
    "    most_active_time = chosen_line['Time'].mode()[0]\n",
    "    # the result is 2:14 PM so I'll type it by hand for now.\n",
    "    st.markdown(\n",
    "        \"\"\"\n",
    "        <div class=\"subheader\">Top Stats</div>\n",
    "        <div class=\"top-stats\">\n",
    "            <div class=\"stat\">\n",
    "                <p>Total Invoices<br><span> %d </span></p>\n",
    "            </div>\n",
    "            <div class=\"stat\">\n",
    "                <p>Average Rating<br><span> %.2f </span></p>\n",
    "            </div>\n",
    "            <div class=\"stat\">\n",
    "                <p>Most Active Time<br><span> %s </span></p>\n",
    "            </div>\n",
    "        </div>\n",
    "        \"\"\" % (total_invoices, average_rating, most_active_time),\n",
    "        unsafe_allow_html=True\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [],
   "source": [
    "with midRow:\n",
    "    # Calculate the total income, costs, and profit\n",
    "    depts_income = chosen_line['Total'].sum()\n",
    "    depts_costs = chosen_line['cogs'].sum()\n",
    "    depts_profit = depts_income - depts_costs\n",
    "\n",
    "    st.markdown(\n",
    "        \"\"\"\n",
    "        <div class=\"top-stats\">\n",
    "            <div class=\"stat\" style=\"background-color: #093b09;\">\n",
    "                <p>Income<br><span>&pound; %.1f</span></p>\n",
    "            </div>\n",
    "            <div class=\"stat\" style=\"background-color: #4e0000;\">\n",
    "                <p>Costs<br><span>&pound; %.1f</span></p>\n",
    "            </div>\n",
    "            <div class=\"stat\" style=\"background-color: #000062;\">\n",
    "                <p>Profit<br><span>&pound; %.1f</span></p>\n",
    "            </div>\n",
    "        </div>\n",
    "        \"\"\" % (depts_income, depts_costs, depts_profit),\n",
    "        unsafe_allow_html=True\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\PC\\AppData\\Local\\Temp\\ipykernel_1264\\3489548866.py:4: UserWarning:\n",
      "\n",
      "Could not infer format, so each element will be parsed individually, falling back to `dateutil`. To ensure parsing is consistent and as-expected, please specify a format.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#Create Dashboard Sections\n",
    "with chartRow:\n",
    "    #Filter for the month\n",
    "    df['Time'] = pd.to_datetime(df['Time'])\n",
    "    mar_data = (df['Time'].dt.month == 3)\n",
    "    lineQuantity = chosen_line[(mar_data)]\n",
    "    \n",
    "    #Quantity for each day\n",
    "    quantity_per_day = lineQuantity.groupby('Time')['Quantity'].sum().reset_index()\n",
    "    \n",
    "    st.markdown('<div></div>', unsafe_allow_html=True)\n",
    "    \n",
    "    #Create a line chart for quantity over the last month using plotly\n",
    "    fig_quantity = px.line(\n",
    "        quantity_per_day,\n",
    "        x='Time',\n",
    "        y='Quantity',\n",
    "        title='Quantity Sold over the Last Month'\n",
    "    )\n",
    "    fig_quantity.update_layout(\n",
    "        margin_r=100,\n",
    "    )\n",
    "    st.plotly_chart(fig_quantity)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [],
   "source": [
    "with footer:\n",
    "    st.markdown('__')\n",
    "    st.markdown(\n",
    "        '''\n",
    "        <style>\n",
    "            p{\n",
    "                font-size: 16px;\n",
    "                text-align: center;\n",
    "            }\n",
    "            a {\n",
    "                text-decoration: none;\n",
    "                color: #00a;\n",
    "                font-weight: 600;\n",
    "            }\n",
    "        </style>\n",
    "        <p>\n",
    "            Design borrowed\n",
    "        </p>\n",
    "        ''', unsafe_allow_html=True\n",
    "    )"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
