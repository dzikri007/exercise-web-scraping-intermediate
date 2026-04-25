import pandas as pd

def transform_to_DataFrame(data):
    """Mengubah data menjadi DataFrame."""
    return pd.DataFrame(data)

def transform_data(data, exchange_rate):
    """Menggabungkan semua transformasi data menjadi satu fungsi."""
    
    # 🔥 Fix Price (handle encoding issue)
    data['Price_in_pounds'] = data['Price'].str.replace(r'[^\d.]', '', regex=True).astype(float)
    
    # 🔥 Transformasi Rating
    rating_mapping = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    data['Rating'] = data['Rating'].replace(rating_mapping).astype(int)
    
    # 🔥 Convert ke rupiah
    data['Price_in_rupiah'] = (data['Price_in_pounds'] * exchange_rate).astype(int)
    
    # 🔥 Hapus kolom lama
    data = data.drop(columns=['Price'])
    
    # 🔥 Tipe data
    data['Title'] = data['Title'].astype('string')
    data['Availability'] = data['Availability'].astype('string')
    
    # 🔥 WAJIB: urutan kolom biar sama persis
    data = data[['Title', 'Availability', 'Rating', 'Price_in_pounds', 'Price_in_rupiah']]
    
    return data