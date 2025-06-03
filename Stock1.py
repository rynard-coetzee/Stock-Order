from pathlib import Path  # Python Standard Library
#from PIL import Image

import pandas as pd  # pip install pandas
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Stock Order",
                   page_icon=":bar_chart:"
)

df = pd.read_csv("Order.csv")
#image = Image.open('Bowler_Logo.jpg')  
#new_image = image.resize((600, 400))

st.sidebar.header("Select Product/Quantity Here:")
st.sidebar.image(new_image)
options_form = st.sidebar.form("options_form")

Product = options_form.selectbox(
        "Select the Product:", ('Amarula', 'Amstel Dumpies', 'Amstel Quarts', 'Amstel Raddler', 'Appletiser', 'Bacardi', 'Belgravia Blood Orange', 'Belgravia Gin & Dry Lemon', 'Belgravia Pink Gin Mix', 'Bells', 'Black Label Dumpies', 'Black Label Quarts', 'Cactus Jack', 'Cape to Rio Cane', 'Captain Morgan', 'Carribean Twist Pina Colada', 'Castle Dumpies', 'Castle Lite Dumpies', 'Castle Lite Quarts', 'Castle Milk Stout Quarts', 'Castle Quarts', 'Coke', 'Coke Light', 'Coke Zero', 'Cookies & Cream', 'Creme Soda', 'Drostdy Hoff Extra Light White 5L', 'Dry Lemon', 'Famous Grouse', 'Fanta Orange', 'Flying Fish Lemon Dumpies', 'Fruittree Mediteranean', 'Fruittree Orange', 'Ginger Ale', 'Glen Grant', 'Gordons Gin', 'Graca', 'Guinness' , 'Hansa Dumpies', 'Hansa Quarts', 'Harrier', 'Hunters Dry Dumpies', 'Hunters Dry Quarts', 'Hunters Gold Dumpies', 'J&B', 'Jack Daniels', 'Jaegermeister', 'Jameson', 'Johnny Walker Red', 'Kahlua', 'Klipdrift', 'Klipdrift Premium', 'Label5', 'Lemonade', 'Lime Cordial' , 'Lion Quarts', 'Malibu', 'Olaf Bergh', 'Old Brown Sherry', 'Passion Fruit Cordial' , 'Peppermint Liquer', 'Pimms', 'PO10c', 'Ponchos', 'Porcupine Ridge Sauv Blanc', 'Powerade Jagged Ice', 'Powerade Mountain Blast', 'Powerade Naartjie', 'Pushkin Apple', 'Red Heart', 'Red Square Energiser', 'Redbull', 'Richlieu', 'Robertsons Dry Red 500ml', 'Robertsons Dry White 500ml', 'Savanah Dry', 'Savanah Light', 'Savanah 0' , 'Scottish Leader', 'Smirnoff Vodka', 'Soda Water', 'Southern Comfort', 'Sparberry', 'Spiced Gold', 'Sprite', 'Sprite Zero', 'Stoney Ginger', 'Strawberry Lips', 'Sunkissed Rose', 'Tall Horse Merlot', 'Tequila Gold Olmeca', 'Tequila Silver Olmeca', 'Tomato Cocktail', 'Tonic', 'Valpre Sparkling Water', 'Valpre Still Water', 'Vat69', 'Windhoek Draught Dumpies', 'Windhoek Draught Quarts', 'Windhoek Lager Quarts'))

Quantity = options_form.text_input(
        "Enter the Amount:")
Type = options_form.radio(
        "Select type:",('Bottle', 'Box' , 'Case'))
add_data = options_form.form_submit_button()
if add_data:
    new_data = {"Product": Product, "Quantity": int(Quantity) ,"Type": Type}
    df = df.append(new_data, ignore_index=True)
    df.to_csv("Order.csv", index=False)
    

if st.sidebar.button('Clear'):
    df = df[0:0]
    df.to_csv("Order.csv", index=False)
    
st.table(df.sort_values(by="Product"))
  
