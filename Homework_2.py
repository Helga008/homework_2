{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "cbc68bf9",
   "metadata": {},
   "source": [
    "## Условие 1: 1 задача\n",
    "\n",
    "Скачать файл в уроке\n",
    "\n",
    "Считать данные с помощью pandas\n",
    "\n",
    "Вывести на экран первые 5 строк\n",
    "\n",
    "Посмотреть на описание признаков и на их содержание\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a6a03859",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "584249c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('kc_house_data.csv', sep=',', encoding='windows-1251')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c3b9a9ed",
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
       "      <th>id</th>\n",
       "      <th>date</th>\n",
       "      <th>price</th>\n",
       "      <th>bedrooms</th>\n",
       "      <th>bathrooms</th>\n",
       "      <th>sqft_living</th>\n",
       "      <th>sqft_lot</th>\n",
       "      <th>floors</th>\n",
       "      <th>waterfront</th>\n",
       "      <th>view</th>\n",
       "      <th>...</th>\n",
       "      <th>grade</th>\n",
       "      <th>sqft_above</th>\n",
       "      <th>sqft_basement</th>\n",
       "      <th>yr_built</th>\n",
       "      <th>yr_renovated</th>\n",
       "      <th>zipcode</th>\n",
       "      <th>lat</th>\n",
       "      <th>long</th>\n",
       "      <th>sqft_living15</th>\n",
       "      <th>sqft_lot15</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>7129300520</td>\n",
       "      <td>20141013T000000</td>\n",
       "      <td>221900.0</td>\n",
       "      <td>3</td>\n",
       "      <td>1.00</td>\n",
       "      <td>1180</td>\n",
       "      <td>5650</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>7</td>\n",
       "      <td>1180.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1955</td>\n",
       "      <td>0</td>\n",
       "      <td>98178</td>\n",
       "      <td>47.5112</td>\n",
       "      <td>-122.257</td>\n",
       "      <td>1340</td>\n",
       "      <td>5650</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>6414100192</td>\n",
       "      <td>20141209T000000</td>\n",
       "      <td>538000.0</td>\n",
       "      <td>3</td>\n",
       "      <td>2.25</td>\n",
       "      <td>2570</td>\n",
       "      <td>7242</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>7</td>\n",
       "      <td>2170.0</td>\n",
       "      <td>400</td>\n",
       "      <td>1951</td>\n",
       "      <td>1991</td>\n",
       "      <td>98125</td>\n",
       "      <td>47.7210</td>\n",
       "      <td>-122.319</td>\n",
       "      <td>1690</td>\n",
       "      <td>7639</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5631500400</td>\n",
       "      <td>20150225T000000</td>\n",
       "      <td>180000.0</td>\n",
       "      <td>2</td>\n",
       "      <td>1.00</td>\n",
       "      <td>770</td>\n",
       "      <td>10000</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>6</td>\n",
       "      <td>770.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1933</td>\n",
       "      <td>0</td>\n",
       "      <td>98028</td>\n",
       "      <td>47.7379</td>\n",
       "      <td>-122.233</td>\n",
       "      <td>2720</td>\n",
       "      <td>8062</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2487200875</td>\n",
       "      <td>20141209T000000</td>\n",
       "      <td>604000.0</td>\n",
       "      <td>4</td>\n",
       "      <td>3.00</td>\n",
       "      <td>1960</td>\n",
       "      <td>5000</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>7</td>\n",
       "      <td>1050.0</td>\n",
       "      <td>910</td>\n",
       "      <td>1965</td>\n",
       "      <td>0</td>\n",
       "      <td>98136</td>\n",
       "      <td>47.5208</td>\n",
       "      <td>-122.393</td>\n",
       "      <td>1360</td>\n",
       "      <td>5000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1954400510</td>\n",
       "      <td>20150218T000000</td>\n",
       "      <td>510000.0</td>\n",
       "      <td>3</td>\n",
       "      <td>2.00</td>\n",
       "      <td>1680</td>\n",
       "      <td>8080</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>8</td>\n",
       "      <td>1680.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1987</td>\n",
       "      <td>0</td>\n",
       "      <td>98074</td>\n",
       "      <td>47.6168</td>\n",
       "      <td>-122.045</td>\n",
       "      <td>1800</td>\n",
       "      <td>7503</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "           id             date     price  bedrooms  bathrooms  sqft_living  \\\n",
       "0  7129300520  20141013T000000  221900.0         3       1.00         1180   \n",
       "1  6414100192  20141209T000000  538000.0         3       2.25         2570   \n",
       "2  5631500400  20150225T000000  180000.0         2       1.00          770   \n",
       "3  2487200875  20141209T000000  604000.0         4       3.00         1960   \n",
       "4  1954400510  20150218T000000  510000.0         3       2.00         1680   \n",
       "\n",
       "   sqft_lot  floors  waterfront  view  ...  grade  sqft_above  sqft_basement  \\\n",
       "0      5650     1.0           0     0  ...      7      1180.0              0   \n",
       "1      7242     2.0           0     0  ...      7      2170.0            400   \n",
       "2     10000     1.0           0     0  ...      6       770.0              0   \n",
       "3      5000     1.0           0     0  ...      7      1050.0            910   \n",
       "4      8080     1.0           0     0  ...      8      1680.0              0   \n",
       "\n",
       "   yr_built  yr_renovated  zipcode      lat     long  sqft_living15  \\\n",
       "0      1955             0    98178  47.5112 -122.257           1340   \n",
       "1      1951          1991    98125  47.7210 -122.319           1690   \n",
       "2      1933             0    98028  47.7379 -122.233           2720   \n",
       "3      1965             0    98136  47.5208 -122.393           1360   \n",
       "4      1987             0    98074  47.6168 -122.045           1800   \n",
       "\n",
       "   sqft_lot15  \n",
       "0        5650  \n",
       "1        7639  \n",
       "2        8062  \n",
       "3        5000  \n",
       "4        7503  \n",
       "\n",
       "[5 rows x 21 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "30a11d0b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 21613 entries, 0 to 21612\n",
      "Data columns (total 21 columns):\n",
      " #   Column         Non-Null Count  Dtype  \n",
      "---  ------         --------------  -----  \n",
      " 0   id             21613 non-null  int64  \n",
      " 1   date           21613 non-null  object \n",
      " 2   price          21613 non-null  float64\n",
      " 3   bedrooms       21613 non-null  int64  \n",
      " 4   bathrooms      21613 non-null  float64\n",
      " 5   sqft_living    21613 non-null  int64  \n",
      " 6   sqft_lot       21613 non-null  int64  \n",
      " 7   floors         21613 non-null  float64\n",
      " 8   waterfront     21613 non-null  int64  \n",
      " 9   view           21613 non-null  int64  \n",
      " 10  condition      21613 non-null  int64  \n",
      " 11  grade          21613 non-null  int64  \n",
      " 12  sqft_above     21611 non-null  float64\n",
      " 13  sqft_basement  21613 non-null  int64  \n",
      " 14  yr_built       21613 non-null  int64  \n",
      " 15  yr_renovated   21613 non-null  int64  \n",
      " 16  zipcode        21613 non-null  int64  \n",
      " 17  lat            21613 non-null  float64\n",
      " 18  long           21613 non-null  float64\n",
      " 19  sqft_living15  21613 non-null  int64  \n",
      " 20  sqft_lot15     21613 non-null  int64  \n",
      "dtypes: float64(6), int64(14), object(1)\n",
      "memory usage: 3.5+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8a7ea3f4",
   "metadata": {},
   "source": [
    "## Условие 2: 2 задача\n",
    "\n",
    "Проведите первичный анализ данных\n",
    "\n",
    "Изучите типы данных\n",
    "\n",
    "Найдите количество пропущенных ячеек в данных\n",
    "\n",
    "Посчитайте основные статистики по всем признакам и поизучайте их\n",
    "\n",
    "Пишите выводы\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d8010cb0",
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
       "      <th>id</th>\n",
       "      <th>price</th>\n",
       "      <th>bedrooms</th>\n",
       "      <th>bathrooms</th>\n",
       "      <th>sqft_living</th>\n",
       "      <th>sqft_lot</th>\n",
       "      <th>floors</th>\n",
       "      <th>waterfront</th>\n",
       "      <th>view</th>\n",
       "      <th>condition</th>\n",
       "      <th>grade</th>\n",
       "      <th>sqft_above</th>\n",
       "      <th>sqft_basement</th>\n",
       "      <th>yr_built</th>\n",
       "      <th>yr_renovated</th>\n",
       "      <th>zipcode</th>\n",
       "      <th>lat</th>\n",
       "      <th>long</th>\n",
       "      <th>sqft_living15</th>\n",
       "      <th>sqft_lot15</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>2.161300e+04</td>\n",
       "      <td>2.161300e+04</td>\n",
       "      <td>21613.000000</td>\n",
       "      <td>21613.000000</td>\n",
       "      <td>21613.000000</td>\n",
       "      <td>2.161300e+04</td>\n",
       "      <td>21613.000000</td>\n",
       "      <td>21613.000000</td>\n",
       "      <td>21613.000000</td>\n",
       "      <td>21613.000000</td>\n",
       "      <td>21613.000000</td>\n",
       "      <td>21611.000000</td>\n",
       "      <td>21613.000000</td>\n",
       "      <td>21613.000000</td>\n",
       "      <td>21613.000000</td>\n",
       "      <td>21613.000000</td>\n",
       "      <td>21613.000000</td>\n",
       "      <td>21613.000000</td>\n",
       "      <td>21613.000000</td>\n",
       "      <td>21613.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>4.580302e+09</td>\n",
       "      <td>5.400881e+05</td>\n",
       "      <td>3.370842</td>\n",
       "      <td>2.114757</td>\n",
       "      <td>2079.899736</td>\n",
       "      <td>1.510697e+04</td>\n",
       "      <td>1.494309</td>\n",
       "      <td>0.007542</td>\n",
       "      <td>0.234303</td>\n",
       "      <td>3.409430</td>\n",
       "      <td>7.656873</td>\n",
       "      <td>1788.396095</td>\n",
       "      <td>291.509045</td>\n",
       "      <td>1971.005136</td>\n",
       "      <td>84.402258</td>\n",
       "      <td>98077.939805</td>\n",
       "      <td>47.560053</td>\n",
       "      <td>-122.213896</td>\n",
       "      <td>1986.552492</td>\n",
       "      <td>12768.455652</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>2.876566e+09</td>\n",
       "      <td>3.671272e+05</td>\n",
       "      <td>0.930062</td>\n",
       "      <td>0.770163</td>\n",
       "      <td>918.440897</td>\n",
       "      <td>4.142051e+04</td>\n",
       "      <td>0.539989</td>\n",
       "      <td>0.086517</td>\n",
       "      <td>0.766318</td>\n",
       "      <td>0.650743</td>\n",
       "      <td>1.175459</td>\n",
       "      <td>828.128162</td>\n",
       "      <td>442.575043</td>\n",
       "      <td>29.373411</td>\n",
       "      <td>401.679240</td>\n",
       "      <td>53.505026</td>\n",
       "      <td>0.138564</td>\n",
       "      <td>0.140828</td>\n",
       "      <td>685.391304</td>\n",
       "      <td>27304.179631</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000102e+06</td>\n",
       "      <td>7.500000e+04</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>290.000000</td>\n",
       "      <td>5.200000e+02</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>290.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1900.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>98001.000000</td>\n",
       "      <td>47.155900</td>\n",
       "      <td>-122.519000</td>\n",
       "      <td>399.000000</td>\n",
       "      <td>651.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2.123049e+09</td>\n",
       "      <td>3.219500e+05</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.750000</td>\n",
       "      <td>1427.000000</td>\n",
       "      <td>5.040000e+03</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>1190.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1951.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>98033.000000</td>\n",
       "      <td>47.471000</td>\n",
       "      <td>-122.328000</td>\n",
       "      <td>1490.000000</td>\n",
       "      <td>5100.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>3.904930e+09</td>\n",
       "      <td>4.500000e+05</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>2.250000</td>\n",
       "      <td>1910.000000</td>\n",
       "      <td>7.618000e+03</td>\n",
       "      <td>1.500000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>1560.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1975.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>98065.000000</td>\n",
       "      <td>47.571800</td>\n",
       "      <td>-122.230000</td>\n",
       "      <td>1840.000000</td>\n",
       "      <td>7620.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>7.308900e+09</td>\n",
       "      <td>6.450000e+05</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>2.500000</td>\n",
       "      <td>2550.000000</td>\n",
       "      <td>1.068800e+04</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>2210.000000</td>\n",
       "      <td>560.000000</td>\n",
       "      <td>1997.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>98118.000000</td>\n",
       "      <td>47.678000</td>\n",
       "      <td>-122.125000</td>\n",
       "      <td>2360.000000</td>\n",
       "      <td>10083.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>9.900000e+09</td>\n",
       "      <td>7.700000e+06</td>\n",
       "      <td>33.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>13540.000000</td>\n",
       "      <td>1.651359e+06</td>\n",
       "      <td>3.500000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>13.000000</td>\n",
       "      <td>9410.000000</td>\n",
       "      <td>4820.000000</td>\n",
       "      <td>2015.000000</td>\n",
       "      <td>2015.000000</td>\n",
       "      <td>98199.000000</td>\n",
       "      <td>47.777600</td>\n",
       "      <td>-121.315000</td>\n",
       "      <td>6210.000000</td>\n",
       "      <td>871200.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 id         price      bedrooms     bathrooms   sqft_living  \\\n",
       "count  2.161300e+04  2.161300e+04  21613.000000  21613.000000  21613.000000   \n",
       "mean   4.580302e+09  5.400881e+05      3.370842      2.114757   2079.899736   \n",
       "std    2.876566e+09  3.671272e+05      0.930062      0.770163    918.440897   \n",
       "min    1.000102e+06  7.500000e+04      0.000000      0.000000    290.000000   \n",
       "25%    2.123049e+09  3.219500e+05      3.000000      1.750000   1427.000000   \n",
       "50%    3.904930e+09  4.500000e+05      3.000000      2.250000   1910.000000   \n",
       "75%    7.308900e+09  6.450000e+05      4.000000      2.500000   2550.000000   \n",
       "max    9.900000e+09  7.700000e+06     33.000000      8.000000  13540.000000   \n",
       "\n",
       "           sqft_lot        floors    waterfront          view     condition  \\\n",
       "count  2.161300e+04  21613.000000  21613.000000  21613.000000  21613.000000   \n",
       "mean   1.510697e+04      1.494309      0.007542      0.234303      3.409430   \n",
       "std    4.142051e+04      0.539989      0.086517      0.766318      0.650743   \n",
       "min    5.200000e+02      1.000000      0.000000      0.000000      1.000000   \n",
       "25%    5.040000e+03      1.000000      0.000000      0.000000      3.000000   \n",
       "50%    7.618000e+03      1.500000      0.000000      0.000000      3.000000   \n",
       "75%    1.068800e+04      2.000000      0.000000      0.000000      4.000000   \n",
       "max    1.651359e+06      3.500000      1.000000      4.000000      5.000000   \n",
       "\n",
       "              grade    sqft_above  sqft_basement      yr_built  yr_renovated  \\\n",
       "count  21613.000000  21611.000000   21613.000000  21613.000000  21613.000000   \n",
       "mean       7.656873   1788.396095     291.509045   1971.005136     84.402258   \n",
       "std        1.175459    828.128162     442.575043     29.373411    401.679240   \n",
       "min        1.000000    290.000000       0.000000   1900.000000      0.000000   \n",
       "25%        7.000000   1190.000000       0.000000   1951.000000      0.000000   \n",
       "50%        7.000000   1560.000000       0.000000   1975.000000      0.000000   \n",
       "75%        8.000000   2210.000000     560.000000   1997.000000      0.000000   \n",
       "max       13.000000   9410.000000    4820.000000   2015.000000   2015.000000   \n",
       "\n",
       "            zipcode           lat          long  sqft_living15     sqft_lot15  \n",
       "count  21613.000000  21613.000000  21613.000000   21613.000000   21613.000000  \n",
       "mean   98077.939805     47.560053   -122.213896    1986.552492   12768.455652  \n",
       "std       53.505026      0.138564      0.140828     685.391304   27304.179631  \n",
       "min    98001.000000     47.155900   -122.519000     399.000000     651.000000  \n",
       "25%    98033.000000     47.471000   -122.328000    1490.000000    5100.000000  \n",
       "50%    98065.000000     47.571800   -122.230000    1840.000000    7620.000000  \n",
       "75%    98118.000000     47.678000   -122.125000    2360.000000   10083.000000  \n",
       "max    98199.000000     47.777600   -121.315000    6210.000000  871200.000000  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5d2d12f3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3734f1ec",
   "metadata": {},
   "source": [
    "## Условие 3: 3 задача\n",
    "\n",
    "Ответьте на несколько вопросов\n",
    "\n",
    "3.1 В каком диапазоне изменяются стоимости недвижимости?\n",
    "\n",
    "3.2 Какую долю в среднем занимают жилая площадь от всей площади по всем домам?\n",
    "\n",
    "3.3 Как много домов с разными этажами в данных?\n",
    "\n",
    "3.4 Насколько хорошие состояния у домов в данных?\n",
    "\n",
    "3.5 Найдите года, когда построили первый дом, когда построили последний дом в данных?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "5b322b36",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "75000.0"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "min_cost = df['price'].min()\n",
    "min_cost"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ce9808ab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7700000.0"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "max_cost = df['price'].max()\n",
    "max_cost"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "e444084d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Стоимость недвижимости меняется от 75000.0 до 7700000.0\n"
     ]
    }
   ],
   "source": [
    "print(f'Стоимость недвижимости меняется от {min_cost} до {max_cost}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "05c1fd64",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "13.76781757959227"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 3.2 Какую долю в среднем занимают жилая площадь от всей площади по всем домам?\n",
    "df['sqft_living'].mean() * 100 / df['sqft_lot'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "7615b645",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0    10680\n",
       "2.0     8241\n",
       "1.5     1910\n",
       "3.0      613\n",
       "2.5      161\n",
       "3.5        8\n",
       "Name: floors, dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## 3.3 Как много домов с разными этажами в данных?\n",
    "df['floors'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "7bd323f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3    14031\n",
       "4     5679\n",
       "5     1701\n",
       "2      172\n",
       "1       30\n",
       "Name: condition, dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#3.4 Насколько хорошие состояния у домов в данных?\n",
    "df['condition'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "902a540c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1900, 2015)"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Найдите года, когда построили первый дом, когда построили последний дом в данных?\n",
    "df['yr_built'].min(), df['yr_built'].max()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "01176c06",
   "metadata": {},
   "source": [
    "## Условие 4: 4 задача\n",
    "\n",
    "\n",
    "4.1 Сколько в среднем стоят дома, у которых 2 спальни?\n",
    "\n",
    "4.2 Какая в среднем общая площадь домов, у которых стоимость больше 600 000?\n",
    "\n",
    "4.3 Как много домов коснулся ремонт?\n",
    "\n",
    "4.4 Насколько в среднем стоимость домов с оценкой grade домов выше 10 отличается от стоимости домов с оценкой grade меньше 4?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "35c312fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "401372.681884058"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Сколько в среднем стоят дома, у которых 2 спальни?\n",
    "df[df['bedrooms'] == 2]['price'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "d6f1ddb0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2444.87450039968"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Какая в среднем общая площадь домов, у которых стоимость больше 600 000?\n",
    "df[df['price'] > 600000]['sqft_above'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "b25939b5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "914"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Как много домов коснулся ремонт?\n",
    "df[df['yr_renovated'] > 0].value_counts().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "4d8ca6f7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1488885.1175298805"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Насколько в среднем стоимость домов с оценкой grade домов выше 10 отличается от стоимости домов с оценкой grade меньше 4?\n",
    "df[df['grade'] > 10]['price'].mean() - df[df['grade'] < 4]['price'].mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fc55fdd3",
   "metadata": {},
   "source": [
    "## Условие 5: 5 задача\n",
    "\n",
    "\n",
    "5.1 Выберите дом клиенту\n",
    "Клиент хочет дом с видом на набережную, как минимум с тремя ванными и с подвалом. Сколько вариантов есть у клиента?\n",
    "\n",
    "5.2 Выберите дом клиенту\n",
    "Клиент хочет дом либо с очень красивым видом из окна, либо с видом на набережную, в очень хорошем состоянии и год постройки не меньше 1980 года. В какой ценовом диапазоне будут дома?\n",
    "\n",
    "5.3 Выберите дом клиенту\n",
    "Клиент хочет дом без подвала, с двумя этажами, стоимостью до 150000. Какая оценка по состоянию у таких домов в среднем?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "9e4ca82e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "41"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[(df['waterfront'] == 1) & (df['bathrooms'] >= 3) & (df['sqft_basement'] > 0)].shape[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "c3d2d9e1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(252000.0, 6885000.0)"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 5.2 Выберите дом клиенту Клиент хочет дом либо с очень красивым видом из окна, либо с видом на набережную, \n",
    "# в очень хорошем состоянии и год постройки не меньше 1980 года. В какой ценовом диапазоне будут дома?\n",
    "\n",
    "df[(df['view'] == 4) | (df['waterfront'] == 1) & (df['condition'] == 5) & (df['yr_built'] >= 1980)]['price'].min(), df[(df['view'] == 4) | (df['waterfront'] == 1) & (df['condition'] == 5) & (df['yr_built'] >= 1980)]['price'].max()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "56e18949",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.8333333333333335"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 5.3 Выберите дом клиенту Клиент хочет дом без подвала, \n",
    "# с двумя этажами, стоимостью до 150000. Какая оценка по состоянию у таких домов в среднем?\n",
    "df[(df['sqft_basement'] == 0) & (df['floors'] == 2)\n",
    "    & (df['price'] < 150000)]['condition'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1ed8612",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
