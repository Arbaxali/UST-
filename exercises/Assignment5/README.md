## 2) display the fileds

````````
{'_id': ObjectId('636354ec47af48663a29657f'), 'address': {'building': '1267', 'coord': [-73.9206272, 40.837419], 'street': 'Jerome Avenue', 
'zipcode': '10452'}, 'borough': 'Bronx', 'cuisine': 'Spanish', 'grades': [{'date': {'$date': 1391644800000}, 'grade': 'A', 'score': 8}, {'date': {'$date': 1373241600000}, 'grade': 'B', 'score': 16}, {'date': {'$date': 1359331200000}, 'grade': 'A', 'score': 5}], 'name': 'Elvalle Restaurant Sport Bar', 'restaurant_id': '41694156'}
{'_id': ObjectId('636354ec47af48663a296580'), 'address': {'building': '2150', 'coord': [-73.939505, 40.810681], 'street': '5 Avenue', 'zipcode': '10037'}, 'borough': 'Manhattan', 'cuisine': 'Continental', 'grades': [{'date': {'$date': 1386547200000}, 'grade': 'C', 'score': 32}, {'date': {'$date': 1363651200000}, 'grade': 'B', 'score': 27}], 'name': "Harlem On Fifth - Shell'S Bistro", 'restaurant_id': '41694159'}     
{'_id': ObjectId('636354ec47af48663a296581'), 'address': {'building': '144-18', 'coord': [-73.82285329999999, 40.7646561], 'street': 'Northern Boulevard', 'zipcode': '11354'}, 'borough': 'Queens', 'cuisine': 'Chinese', 'grades': [{'date': {'$date': 1418601600000}, 'grade': 'A', 'score': 12}, {'date': {'$date': 1401926400000}, 'grade': 'A', 'score': 8}, {'date': {'$date': 1385942400000}, 'grade': 'A', 'score': 10}, {'date': {'$date': 1367193600000}, 'grade': 'A', 'score': 9}], 'name': 'Chun Buro Restaurant', 'restaurant_id': '41694167'}
{'_id': ObjectId('636354ec47af48663a296582'), 'address': {'building': '115', 'coord': [-73.9585845, 40.71879879999999], 'street': 'Berry Street', 'zipcode': '11249'}, 'borough': 'Brooklyn', 'cuisine': 'Italian', 'grades': [{'date': {'$date': 1405987200000}, 'grade': 'A', 'score': 12}, {'date': {'$date': 1391040000000}, 'grade': 'A', 'score': 12}, {'date': {'$date': 1382313600000}, 'grade': 'P', 'score': 2}, {'date': 
{'$date': 1365120000000}, 'grade': 'B', 'score': 17}], 'name': 'Antica Pesa', 'restaurant_id': '41694170'}
{'_id': ObjectId('636354ec47af48663a296583'), 'address': {'building': '1836', 'coord': [-73.8937725, 40.6371227], 'street': 'Rockaway Parkway', 'zipcode': '11236'}, 'borough': 'Brooklyn', 'cuisine': 'Bakery', 'grades': [{'date': {'$date': 1395273600000}, 'grade': 'A', 'score': 2}, {'date': {'$date': 1363132800000}, 'grade': 'A', 'score': 2}], 'name': 'La Baguette Shop', 'restaurant_id': '41694199'}
{'_id': ObjectId('636354ec47af48663a296584'), 'address': {'building': '75-63', 'coord': [-73.8919493, 40.7602115], 'street': '31 Avenue', 'zipcode': '11370'}, 'borough': 'Queens', 'cuisine': 'Italian', 'grades': [{'date': {'$date': 1402531200000}, 'grade': 'A', 'score': 9}, {'date': {'$date': 1383523200000}, 'grade': 'B', 'score': 15}, {'date': {'$date': 1361318400000}, 'grade': 'B', 'score': 23}], 'name': "Mr. Bruno'S Pizza", 'restaurant_id': '41694244'}
{'_id': ObjectId('636354ec47af48663a296585'), 'address': {'building': '1693', 'coord': [-73.94812759999999, 40.8245061], 'street': 'Amsterdam Avenue', 'zipcode': '10031'}, 'borough': 'Manhattan', 'cuisine': 'Mexican', 'grades': [{'date': {'$date': 1420156800000}, 'grade': 'A', 'score': 12}, {'date': {'$date': 1403913600000}, 'grade': 'A', 'score': 4}, {'date': {'$date': 1380499200000}, 'grade': 'A', 'score': 6}, {'date': {'$date': 1358985600000}, 'grade': 'A', 'score': 3}], 'name': 'La Nueva Caricia Restaurant', 'restaurant_id': '41694248'}
.......
.......
.......


````````

## 3) Display the fields restaurant_id, name, borough, and zip code, but exclude the field _id for all the documents in the collection restaurant.



````````
****************************************************************************************************
{'_id': {'RestuarantId': '41552490', 'name': 'Dosa Garden Sri Lanka Restaurant', 'borough': 'Staten Island', 'cuisine': 'Indian'}}
{'_id': {'RestuarantId': '41439359', 'name': 'Kestane Kebab', 'borough': 'Brooklyn', 'cuisine': 'Turkish'}}
{'_id': {'RestuarantId': '41719364', 'name': 'Golden Sand Seafood Restaurant', 'borough': 'Manhattan', 'cuisine': 'Chinese'}}
{'_id': {'RestuarantId': '41638850', 'name': 'Best Lexington Pizza', 'borough': 'Manhattan', 'cuisine': 'Pizza'}}
{'_id': {'RestuarantId': '50002762', 'name': 'Bread & Butter', 'borough': 'Manhattan', 'cuisine': 'American '}}
{'_id': {'RestuarantId': '41665255', 'name': "Mchale'S Bar & Grill", 'borough': 'Manhattan', 'cuisine': 'Irish'}}
{'_id': {'RestuarantId': '50000222', 'name': "Papa John'S", 'borough': 'Queens', 'cuisine': 'Pizza'}}
{'_id': {'RestuarantId': '41365330', 'name': "New Everybody'S Kitchen", 'borough': 'Staten Island', 'cuisine': 'Chinese'}}
{'_id': {'RestuarantId': '50016120', 'name': 'Billet And Bellows', 'borough': 'Brooklyn', 'cuisine': 'Not Listed/Not Applicable'}}
{'_id': {'RestuarantId': '41413717', 'name': "Samantha'S Southern Cuisine", 'borough': 'Brooklyn', 'cuisine': 'American '}}
{'_id': {'RestuarantId': '41627984', 'name': 'Jouvay Night Club', 'borough': 'Queens', 'cuisine': 'Caribbean'}}
{'_id': {'RestuarantId': '50017893', 'name': 'Sake Bomb', 'borough': 'Queens', 'cuisine': 'Other'}}
{'_id': {'RestuarantId': '41602559', 'name': 'Red Chopstick', 'borough': 'Queens', 'cuisine': 'Chinese'}}
{'_id': {'RestuarantId': '40978782', 'name': 'The Mark Bar', 'borough': 'Brooklyn', 'cuisine': 'American '}}
{'_id': {'RestuarantId': '41487544', 'name': 'Nanoosh', 'borough': 'Manhattan', 'cuisine': 'Mediterranean'}}
{'_id': {'RestuarantId': '50005075', 'name': 'Apple Jack Diner', 'borough': 'Manhattan', 'cuisine': 'American '}}
{'_id': {'RestuarantId': '50010461', 'name': 'Island Salad', 'borough': 'Brooklyn', 'cuisine': 'Salads'}}
{'_id': {'RestuarantId': '40399256', 'name': 'Singas Famous Pizza', 'borough': 'Queens', 'cuisine': 'Pizza'}}
{'_id': {'RestuarantId': '50012527', 'name': 'Uglyducking', 'borough': 'Brooklyn', 'cuisine': 'American '}}
{'_id': {'RestuarantId': '41383227', 'name': 'La Nazionale Soccer Club', 'borough': 'Queens', 'cuisine': 'Italian'}}
****************************************************************************************************

````````

## 4).Find the restaurants who achieved a score more than 90. (LIMTI-25)

````````
****************************************************************************************************
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 11}, {'score': 131}, {'score': 11}, {'score': 25}, {'score': 11}, {'score': 13}], 'name': "Murals On 54/Randolphs'S", 'restaurant_id': '40372466'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 5}, {'score': 8}, {'score': 12}, {'score': 2}, {'score': 9}, {'score': 92}, {'score': 41}], 'name': 'Gandhi', 'restaurant_id': '40381295'}
{'borough': 'Manhattan', 'cuisine': 'Pizza/Italian', 'grades': [{'score': 31}, {'score': 98}, {'score': 32}, {'score': 21}, {'score': 11}], 
'name': 'Bella Napoli', 'restaurant_id': '40393488'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 7}, {'score': 12}, {'score': 21}, {'score': 18}, {'score': 11}, {'score': 98}], 'name': "Baluchi'S Indian Food", 'restaurant_id': '41569277'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 11}, {'score': 131}, {'score': 11}, {'score': 25}, {'score': 11}, {'score': 13}], 'name': "Murals On 54/Randolphs'S", 'restaurant_id': '40372466'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 5}, {'score': 8}, {'score': 12}, {'score': 2}, {'score': 9}, {'score': 92}, {'score': 41}], 'name': 'Gandhi', 'restaurant_id': '40381295'}
{'borough': 'Manhattan', 'cuisine': 'Pizza/Italian', 'grades': [{'score': 31}, {'score': 98}, {'score': 32}, {'score': 21}, {'score': 11}], 
'name': 'Bella Napoli', 'restaurant_id': '40393488'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 7}, {'score': 12}, {'score': 21}, {'score': 18}, {'score': 11}, {'score': 98}], 'name': "Baluchi'S Indian Food", 'restaurant_id': '41569277'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 11}, {'score': 131}, {'score': 11}, {'score': 25}, {'score': 11}, {'score': 13}], 'name': "Murals On 54/Randolphs'S", 'restaurant_id': '40372466'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 5}, {'score': 8}, {'score': 12}, {'score': 2}, {'score': 9}, {'score': 92}, {'score': 41}], 'name': 'Gandhi', 'restaurant_id': '40381295'}
{'borough': 'Manhattan', 'cuisine': 'Pizza/Italian', 'grades': [{'score': 31}, {'score': 98}, {'score': 32}, {'score': 21}, {'score': 11}], 
'name': 'Bella Napoli', 'restaurant_id': '40393488'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 7}, {'score': 12}, {'score': 21}, {'score': 18}, {'score': 11}, {'score': 98}], 'name': "Baluchi'S Indian Food", 'restaurant_id': '41569277'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 11}, {'score': 131}, {'score': 11}, {'score': 25}, {'score': 11}, {'score': 13}], 'name': "Murals On 54/Randolphs'S", 'restaurant_id': '40372466'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 5}, {'score': 8}, {'score': 12}, {'score': 2}, {'score': 9}, {'score': 92}, {'score': 41}], 'name': 'Gandhi', 'restaurant_id': '40381295'}
{'borough': 'Manhattan', 'cuisine': 'Pizza/Italian', 'grades': [{'score': 31}, {'score': 98}, {'score': 32}, {'score': 21}, {'score': 11}], 
'name': 'Bella Napoli', 'restaurant_id': '40393488'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 7}, {'score': 12}, {'score': 21}, {'score': 18}, {'score': 11}, {'score': 98}], 'name': "Baluchi'S Indian Food", 'restaurant_id': '41569277'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 11}, {'score': 131}, {'score': 11}, {'score': 25}, {'score': 11}, {'score': 13}], 'name': "Murals On 54/Randolphs'S", 'restaurant_id': '40372466'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 5}, {'score': 8}, {'score': 12}, {'score': 2}, {'score': 9}, {'score': 92}, {'score': 41}], 'name': 'Gandhi', 'restaurant_id': '40381295'}
{'borough': 'Manhattan', 'cuisine': 'Pizza/Italian', 'grades': [{'score': 31}, {'score': 98}, {'score': 32}, {'score': 21}, {'score': 11}], 
'name': 'Bella Napoli', 'restaurant_id': '40393488'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 7}, {'score': 12}, {'score': 21}, {'score': 18}, {'score': 11}, {'score': 98}], 'name': "Baluchi'S Indian Food", 'restaurant_id': '41569277'}
****************************************************************************************************

````````
## 5). Show the restaurants that achieved a score, more than 80 but less than 100. (LIMIT-25)


````````

****************************************************************************************************
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 11}, {'score': 131}, {'score': 11}, {'score': 25}, {'score': 11}, {'score': 13}], 'name': "Murals On 54/Randolphs'S", 'restaurant_id': '40372466'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 5}, {'score': 8}, {'score': 12}, {'score': 2}, {'score': 9}, {'score': 92}, {'score': 41}], 'name': 'Gandhi', 'restaurant_id': '40381295'}
{'borough': 'Manhattan', 'cuisine': 'Pizza/Italian', 'grades': [{'score': 31}, {'score': 98}, {'score': 32}, {'score': 21}, {'score': 11}], 
'name': 'Bella Napoli', 'restaurant_id': '40393488'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 89}, {'score': 6}, {'score': 13}], 'name': 'West 79Th Street Boat Basin Cafe', 'restaurant_id': '40756344'}
{'borough': 'Queens', 'cuisine': 'Thai', 'grades': [{'score': 14}, {'score': 84}, {'score': 11}, {'score': 23}], 'name': 'Spicy Shallot', 'restaurant_id': '40979431'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 84}, {'score': 5}, {'score': 10}, {'score': 36}, {'score': 12}, {'score': 27}], 'name': 'Bistro Caterers', 'restaurant_id': '40987023'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 90}, {'score': 27}, {'score': 12}, {'score': 10}], 'name': 'Concrete Restaurant', 'restaurant_id': '41363541'}
{'borough': 'Brooklyn', 'cuisine': 'Italian', 'grades': [{'score': 18}, {'score': 12}, {'score': 24}, {'score': 18}, {'score': 81}], 'name': 'Anella', 'restaurant_id': '41410058'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 7}, {'score': 12}, {'score': 21}, {'score': 18}, {'score': 11}, {'score': 98}], 'name': "Baluchi'S Indian Food", 'restaurant_id': '41569277'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 11}, {'score': 11}, {'score': 82}, {'score': 11}, {'score': 19}, {'score': 29}], 'name': 'Cafe R', 'restaurant_id': '41574642'}
{'borough': 'Brooklyn', 'cuisine': 'Chinese', 'grades': [{'score': 86}, {'score': 20}, {'score': 11}, {'score': 10}], 'name': 'D & Y Restaurant', 'restaurant_id': '50000040'}
{'borough': 'Bronx', 'cuisine': 'Latin (Cuban, Dominican, Puerto Rican, South & Central American)', 'grades': [{'score': 10}, {'score': 82}], 'name': 'La Potencia Restaurant', 'restaurant_id': '50014192'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 11}, {'score': 131}, {'score': 11}, {'score': 25}, {'score': 11}, {'score': 13}], 'name': "Murals On 54/Randolphs'S", 'restaurant_id': '40372466'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 5}, {'score': 8}, {'score': 12}, {'score': 2}, {'score': 9}, {'score': 92}, {'score': 41}], 'name': 'Gandhi', 'restaurant_id': '40381295'}
{'borough': 'Manhattan', 'cuisine': 'Pizza/Italian', 'grades': [{'score': 31}, {'score': 98}, {'score': 32}, {'score': 21}, {'score': 11}], 
'name': 'Bella Napoli', 'restaurant_id': '40393488'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 89}, {'score': 6}, {'score': 13}], 'name': 'West 79Th Street Boat Basin Cafe', 'restaurant_id': '40756344'}
{'borough': 'Queens', 'cuisine': 'Thai', 'grades': [{'score': 14}, {'score': 84}, {'score': 11}, {'score': 23}], 'name': 'Spicy Shallot', 'restaurant_id': '40979431'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 84}, {'score': 5}, {'score': 10}, {'score': 36}, {'score': 12}, {'score': 27}], 'name': 'Bistro Caterers', 'restaurant_id': '40987023'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 90}, {'score': 27}, {'score': 12}, {'score': 10}], 'name': 'Concrete Restaurant', 'restaurant_id': '41363541'}
{'borough': 'Brooklyn', 'cuisine': 'Italian', 'grades': [{'score': 18}, {'score': 12}, {'score': 24}, {'score': 18}, {'score': 81}], 'name': 'Anella', 'restaurant_id': '41410058'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 7}, {'score': 12}, {'score': 21}, {'score': 18}, {'score': 11}, {'score': 98}], 'name': "Baluchi'S Indian Food", 'restaurant_id': '41569277'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 11}, {'score': 11}, {'score': 82}, {'score': 11}, {'score': 19}, {'score': 29}], 'name': 'Cafe R', 'restaurant_id': '41574642'}
{'borough': 'Brooklyn', 'cuisine': 'Chinese', 'grades': [{'score': 86}, {'score': 20}, {'score': 11}, {'score': 10}], 'name': 'D & Y Restaurant', 'restaurant_id': '50000040'}
{'borough': 'Bronx', 'cuisine': 'Latin (Cuban, Dominican, Puerto Rican, South & Central American)', 'grades': [{'score': 10}, {'score': 82}], 'name': 'La Potencia Restaurant', 'restaurant_id': '50014192'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 11}, {'score': 131}, {'score': 11}, {'score': 25}, {'score': 11}, {'score': 13}], 'name': "Murals On 54/Randolphs'S", 'restaurant_id': '40372466'}
****************************************************************************************************

````````

## 6). Write Query to show the restaurants that do not prepare any cuisine of american & their grade score > 70. LIMIT-(50)


`````````
****************************************************************************************************
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '50010813'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '50010813'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Afghan Kebob House', 'restaurant_id': '41535706'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Balkh Shish Kabab House', 'restaurant_id': '50007432'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '41559771'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'New Bkhatar Afghan Halal Kabab & Gyro King', 'restaurant_id': '50001906'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '41559771'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '41559771'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Tariq Afghan Kabab', 'restaurant_id': '50010806'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Choopan Kabab Restaurant', 'restaurant_id': '41569155'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Arya Kabob House', 'restaurant_id': '50008452'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Choopan Kabab Restaurant', 'restaurant_id': '41569155'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Arya Kabob House', 'restaurant_id': '50008452'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Tariq Afghan Kabab', 'restaurant_id': '50010806'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Arya Kabob House', 'restaurant_id': '50008452'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Afghan Kebob House', 'restaurant_id': '41535706'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'New Bkhatar Afghan Halal Kabab & Gyro King', 'restaurant_id': '50001906'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Choopan Kabab Restaurant', 'restaurant_id': '41569155'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhtar Kabab', 'restaurant_id': '41661199'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '41559771'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '50010813'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhtar Kabab', 'restaurant_id': '41661199'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Afghan Kebob House', 'restaurant_id': '41535706'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Afghan Kebob House', 'restaurant_id': '41535706'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Balkh Shish Kabab House', 'restaurant_id': '50007432'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Tariq Afghan Kabab', 'restaurant_id': '50010806'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Afghan Kebob House', 'restaurant_id': '41535706'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '50010813'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Balkh Shish Kabab House', 'restaurant_id': '50007432'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Afghan Kebob House', 'restaurant_id': '41535706'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Tariq Afghan Kabab', 'restaurant_id': '50010806'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Balkh Shish Kabab House', 'restaurant_id': '50007432'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Tariq Afghan Kabab', 'restaurant_id': '50010806'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '41559771'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'New Bkhatar Afghan Halal Kabab & Gyro King', 'restaurant_id': '50001906'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '50010813'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Balkh Shish Kabab House', 'restaurant_id': '50007432'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Choopan Kabab Restaurant', 'restaurant_id': '41569155'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'New Bkhatar Afghan Halal Kabab & Gyro King', 'restaurant_id': '50001906'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Arya Kabob House', 'restaurant_id': '50008452'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'New Bkhatar Afghan Halal Kabab & Gyro King', 'restaurant_id': '50001906'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Choopan Kabab Restaurant', 'restaurant_id': '41569155'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Choopan Kabab Restaurant', 'restaurant_id': '41569155'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhtar Kabab', 'restaurant_id': '41661199'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'New Bkhatar Afghan Halal Kabab & Gyro King', 'restaurant_id': '50001906'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhtar Kabab', 'restaurant_id': '41661199'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '41559771'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Arya Kabob House', 'restaurant_id': '50008452'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhtar Kabab', 'restaurant_id': '41661199'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhtar Kabab', 'restaurant_id': '41661199'}

****************************************************************************************************

`````````

## 7 Write a MongoDB query to arrange the name of the cuisine in an ascending order and for that same borough arranged in descending order.

````````
****************************************************************************************************
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '50010813'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '50010813'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Afghan Kebob House', 'restaurant_id': '41535706'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Balkh Shish Kabab House', 'restaurant_id': '50007432'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '41559771'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'New Bkhatar Afghan Halal Kabab & Gyro King', 'restaurant_id': '50001906'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '41559771'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '41559771'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Tariq Afghan Kabab', 'restaurant_id': '50010806'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Choopan Kabab Restaurant', 'restaurant_id': '41569155'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Arya Kabob House', 'restaurant_id': '50008452'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Choopan Kabab Restaurant', 'restaurant_id': '41569155'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Arya Kabob House', 'restaurant_id': '50008452'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Tariq Afghan Kabab', 'restaurant_id': '50010806'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Arya Kabob House', 'restaurant_id': '50008452'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Afghan Kebob House', 'restaurant_id': '41535706'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'New Bkhatar Afghan Halal Kabab & Gyro King', 'restaurant_id': '50001906'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Choopan Kabab Restaurant', 'restaurant_id': '41569155'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhtar Kabab', 'restaurant_id': '41661199'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '41559771'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '50010813'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhtar Kabab', 'restaurant_id': '41661199'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Afghan Kebob House', 'restaurant_id': '41535706'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Afghan Kebob House', 'restaurant_id': '41535706'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Balkh Shish Kabab House', 'restaurant_id': '50007432'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Tariq Afghan Kabab', 'restaurant_id': '50010806'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Afghan Kebob House', 'restaurant_id': '41535706'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '50010813'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Balkh Shish Kabab House', 'restaurant_id': '50007432'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Afghan Kebob House', 'restaurant_id': '41535706'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Tariq Afghan Kabab', 'restaurant_id': '50010806'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Balkh Shish Kabab House', 'restaurant_id': '50007432'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Tariq Afghan Kabab', 'restaurant_id': '50010806'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '41559771'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'New Bkhatar Afghan Halal Kabab & Gyro King', 'restaurant_id': '50001906'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '50010813'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Balkh Shish Kabab House', 'restaurant_id': '50007432'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Choopan Kabab Restaurant', 'restaurant_id': '41569155'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'New Bkhatar Afghan Halal Kabab & Gyro King', 'restaurant_id': '50001906'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Arya Kabob House', 'restaurant_id': '50008452'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'New Bkhatar Afghan Halal Kabab & Gyro King', 'restaurant_id': '50001906'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Choopan Kabab Restaurant', 'restaurant_id': '41569155'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Choopan Kabab Restaurant', 'restaurant_id': '41569155'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhtar Kabab', 'restaurant_id': '41661199'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'New Bkhatar Afghan Halal Kabab & Gyro King', 'restaurant_id': '50001906'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhtar Kabab', 'restaurant_id': '41661199'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhter Afghan Halal Kabab', 'restaurant_id': '41559771'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Arya Kabob House', 'restaurant_id': '50008452'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhtar Kabab', 'restaurant_id': '41661199'}
{'borough': 'Queens', 'cuisine': 'Afghan', 'name': 'Bakhtar Kabab', 'restaurant_id': '41661199'}
****************************************************************************************************
````````

## 8).Write a MongoDB query to arrange the name of the cuisine in descending order.


````````
****************************************************************************************************
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Pho Bang Restaurant', 'restaurant_id': '41145163'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Home Vietnamese Sandwich And Bubble Tea', 'restaurant_id': '41461382'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Boi Noodle Restaurant', 'restaurant_id': '41473278'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Mekong Brooklyn', 'restaurant_id': '41648717'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Mekong Thai And Vietnamese Restaurant', 'restaurant_id': '41022628'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'A+ Lollipop', 'restaurant_id': '41611605'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Banh Mi Saigon Bakery', 'restaurant_id': '41494286'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Pink Lotus Gourmet', 'restaurant_id': '41486961'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Pho Vietnamese Restaurant', 'restaurant_id': '41379217'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Thai Son', 'restaurant_id': '41221266'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Pho Bang Restaurant', 'restaurant_id': '41338955'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Nha Trang Restaurant', 'restaurant_id': '40989220'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Bia Bar & Grill', 'restaurant_id': '41655832'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'A La Saigon', 'restaurant_id': '41613672'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Sao Mai Vietnamese Cuisine', 'restaurant_id': '41629235'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Nam Nam', 'restaurant_id': '41528836'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'V-Nam Cafe', 'restaurant_id': '41520658'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Co Ba Restaurant', 'restaurant_id': '41483297'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Henry', 'restaurant_id': '41604359'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Pho 32 & Shabu', 'restaurant_id': '41026002'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Baoguette Pho Sure', 'restaurant_id': '41414673'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'O-Mai', 'restaurant_id': '40903063'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'New Gia Lam Vietnamese Food', 'restaurant_id': '41457893'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Lan Cafe', 'restaurant_id': '41184550'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'New Tu Do Restaurant', 'restaurant_id': '41374711'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Nha-Trang Centre Vietnam Restaurant', 'restaurant_id': '40751226'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Pho Bang Restaurant', 'restaurant_id': '40700664'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Thanh Da', 'restaurant_id': '41353290'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Ba Xuyen', 'restaurant_id': '40959591'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Little Thanh Da', 'restaurant_id': '41656294'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Cong Ly Restaurant', 'restaurant_id': '41626364'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': "Luu'S  Baguette", 'restaurant_id': '41627431'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Viet Cafe', 'restaurant_id': '41063946'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Paris Sandwich', 'restaurant_id': '41674140'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Saigon Shack', 'restaurant_id': '41538633'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Saigon Market', 'restaurant_id': '41539844'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Pho Bac Vietnamese Seafood Cuisine', 'restaurant_id': '40578058'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': "Cha Pa'S Vietnamese Eatery", 'restaurant_id': '41551369'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Saigon Vietnamese Sandwich', 'restaurant_id': '41254832'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Saigon 48/ Aoki', 'restaurant_id': '41484659'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Thai Son', 'restaurant_id': '40559606'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Cyclo', 'restaurant_id': '41677087'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'New Mekong Restaurant', 'restaurant_id': '41202673'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'An Choi', 'restaurant_id': '41386399'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Pho Viet', 'restaurant_id': '41695857'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Saiguette', 'restaurant_id': '41677130'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Banh Mi Veitnamese Sandwiches', 'restaurant_id': '41459143'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Pho Grand', 'restaurant_id': '41375457'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Pho Viet-Nam Restaurant', 'restaurant_id': '41158964'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'New Bo Ky Restaurant', 'restaurant_id': '41005330'}
****************************************************************************************************

````````


## 9).Show the restaurant Id, name, borough and cuisines for those restaurants which prepared dish except 'American' and 'Chinese' or restaurant's name begins with letter 'Bil'.


````````
****************************************************************************************************
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Pho Bang Restaurant', 'restaurant_id': '41145163'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Home Vietnamese Sandwich And Bubble Tea', 'restaurant_id': '41461382'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Boi Noodle Restaurant', 'restaurant_id': '41473278'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Mekong Brooklyn', 'restaurant_id': '41648717'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Mekong Thai And Vietnamese Restaurant', 'restaurant_id': '41022628'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'A+ Lollipop', 'restaurant_id': '41611605'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Banh Mi Saigon Bakery', 'restaurant_id': '41494286'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Pink Lotus Gourmet', 'restaurant_id': '41486961'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Pho Vietnamese Restaurant', 'restaurant_id': '41379217'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Thai Son', 'restaurant_id': '41221266'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Pho Bang Restaurant', 'restaurant_id': '41338955'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Nha Trang Restaurant', 'restaurant_id': '40989220'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Bia Bar & Grill', 'restaurant_id': '41655832'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'A La Saigon', 'restaurant_id': '41613672'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Sao Mai Vietnamese Cuisine', 'restaurant_id': '41629235'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Nam Nam', 'restaurant_id': '41528836'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'V-Nam Cafe', 'restaurant_id': '41520658'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Co Ba Restaurant', 'restaurant_id': '41483297'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Henry', 'restaurant_id': '41604359'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Pho 32 & Shabu', 'restaurant_id': '41026002'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Baoguette Pho Sure', 'restaurant_id': '41414673'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'O-Mai', 'restaurant_id': '40903063'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'New Gia Lam Vietnamese Food', 'restaurant_id': '41457893'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Lan Cafe', 'restaurant_id': '41184550'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'New Tu Do Restaurant', 'restaurant_id': '41374711'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Nha-Trang Centre Vietnam Restaurant', 'restaurant_id': '40751226'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Pho Bang Restaurant', 'restaurant_id': '40700664'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Thanh Da', 'restaurant_id': '41353290'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Ba Xuyen', 'restaurant_id': '40959591'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Little Thanh Da', 'restaurant_id': '41656294'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Cong Ly Restaurant', 'restaurant_id': '41626364'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': "Luu'S  Baguette", 'restaurant_id': '41627431'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Viet Cafe', 'restaurant_id': '41063946'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Paris Sandwich', 'restaurant_id': '41674140'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Saigon Shack', 'restaurant_id': '41538633'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Saigon Market', 'restaurant_id': '41539844'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Pho Bac Vietnamese Seafood Cuisine', 'restaurant_id': '40578058'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': "Cha Pa'S Vietnamese Eatery", 'restaurant_id': '41551369'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Saigon Vietnamese Sandwich', 'restaurant_id': '41254832'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Saigon 48/ Aoki', 'restaurant_id': '41484659'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Thai Son', 'restaurant_id': '40559606'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Cyclo', 'restaurant_id': '41677087'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'New Mekong Restaurant', 'restaurant_id': '41202673'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'An Choi', 'restaurant_id': '41386399'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Pho Viet', 'restaurant_id': '41695857'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Saiguette', 'restaurant_id': '41677130'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Banh Mi Veitnamese Sandwiches', 'restaurant_id': '41459143'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Pho Grand', 'restaurant_id': '41375457'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'Pho Viet-Nam Restaurant', 'restaurant_id': '41158964'}
{'cuisine': 'Vietnamese/Cambodian/Malaysia', 'name': 'New Bo Ky Restaurant', 'restaurant_id': '41005330'}
****************************************************************************************************
****************************************************************************************************
{'borough': 'Queens', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018199'}
{'borough': 'Manhattan', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018085'}
{'borough': 'Brooklyn', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018170'}
{'borough': 'Manhattan', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018219'}
{'borough': 'Manhattan', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50017887'}
{'borough': 'Manhattan', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018243'}
{'borough': 'Manhattan', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018083'}
{'borough': 'Manhattan', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018271'}
{'borough': 'Manhattan', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018012'}
{'borough': 'Manhattan', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018088'}
{'borough': 'Brooklyn', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50017967'}
{'borough': 'Manhattan', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018117'}
{'borough': 'Staten Island', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018227'}
{'borough': 'Brooklyn', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018062'}
{'borough': 'Queens', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018292'}
{'borough': 'Brooklyn', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018186'}
{'borough': 'Queens', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018213'}
{'borough': 'Bronx', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50017982'}
{'borough': 'Manhattan', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018293'}
{'borough': 'Brooklyn', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018197'}
{'borough': 'Manhattan', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018269'}
{'borough': 'Brooklyn', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018050'}
{'borough': 'Brooklyn', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018270'}
{'borough': 'Manhattan', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018100'}
{'borough': 'Queens', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018166'}
{'borough': 'Brooklyn', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50017938'}
{'borough': 'Staten Island', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018165'}
{'borough': 'Brooklyn', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018007'}
{'borough': 'Brooklyn', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018061'}
{'borough': 'Staten Island', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018297'}
{'borough': 'Queens', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50017969'}
{'borough': 'Queens', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018095'}
{'borough': 'Bronx', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50017935'}
{'borough': 'Manhattan', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018302'}
{'borough': 'Manhattan', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50017912'}
{'borough': 'Manhattan', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018216'}
{'borough': 'Brooklyn', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018042'}
{'borough': 'Manhattan', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018261'}
{'borough': 'Manhattan', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018128'}
{'borough': 'Manhattan', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018160'}
{'borough': 'Brooklyn', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50017925'}
{'borough': 'Bronx', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018312'}
{'borough': 'Queens', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018141'}
{'borough': 'Manhattan', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018236'}
{'borough': 'Queens', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018322'}
{'borough': 'Brooklyn', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018315'}
{'borough': 'Brooklyn', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018278'}
{'borough': 'Manhattan', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018259'}
{'borough': 'Queens', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50018231'}
{'borough': 'Brooklyn', 'cuisine': 'Other', 'name': '', 'restaurant_id': '50017910'}
****************************************************************************************************


````````

## 10).Show the restaurant Id, name, borough and cuisines and score for restaurant's name begins with letter 'Bil'.

`````````
****************************************************************************************************
{'borough': 'Bronx', 'cuisine': 'American ', 'grades': [{'score': 30}, {'score': 29}, {'score': 33}, {'score': 10}, {'score': 51}], 'name': 
"Billy'S Sport Bar Restaurant & Lounge", 'restaurant_id': '40624470'}
{'borough': 'Queens', 'cuisine': 'American ', 'grades': [{'score': 12}, {'score': 12}, {'score': 16}, {'score': 15}, {'score': 19}, {'score': 11}], 'name': 'Billiard Company', 'restaurant_id': '40717559'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 12}, {'score': 2}, {'score': 13}, {'score': 10}, {'score': 11}, {'score': 14}], 'name': 'Billymarks West', 'restaurant_id': '40785565'}
{'borough': 'Queens', 'cuisine': 'American ', 'grades': [{'score': 7}, {'score': 13}, {'score': 12}, {'score': 9}, {'score': 13}], 'name': "Bill'S Restaurant", 'restaurant_id': '40868248'}
{'borough': 'Brooklyn', 'cuisine': 'American ', 'grades': [{'score': 7}, {'score': 12}, {'score': 9}], 'name': 'Billiard Club', 'restaurant_id': '41013850'}
{'borough': 'Brooklyn', 'cuisine': 'American ', 'grades': [{'score': 2}, {'score': 10}, {'score': 25}, {'score': 12}, {'score': 12}], 'name': "Bill'S Bar", 'restaurant_id': '41089835'}
{'borough': 'Queens', 'cuisine': 'American ', 'grades': [{'score': 4}, {'score': 2}, {'score': 8}, {'score': 9}], 'name': 'Billiard Room', 'restaurant_id': '41150814'}
{'borough': 'Manhattan', 'cuisine': 'Soul Food', 'grades': [{'score': 12}, {'score': 17}, {'score': 11}], 'name': "Billie'S Black Bar Lounge And Restaurant", 'restaurant_id': '41188374'}
{'borough': 'Manhattan', 'cuisine': 'Bakery', 'grades': [{'score': 9}, {'score': 12}, {'score': 12}, {'score': 10}], 'name': "Billy'S Bakery", 'restaurant_id': '41421237'}
{'borough': 'Manhattan', 'cuisine': 'Hamburgers', 'grades': [{'score': 4}, {'score': 11}, {'score': 12}, {'score': 9}], 'name': "Bill'S Bar 
& Burgers", 'restaurant_id': '41444224'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 12}, {'score': 12}, {'score': 12}, {'score': 10}], 'name': 'Billiards', 'restaurant_id': '41447357'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 10}, {'score': 3}, {'score': 9}, {'score': 7}], 'name': "Bill'S Bar & 
Burger Rockefeller Center", 'restaurant_id': '41509909'}
{'borough': 'Manhattan', 'cuisine': 'Bakery', 'grades': [{'score': 9}, {'score': 13}, {'score': 8}, {'score': 7}, {'score': 31}], 'name': "Billy'S Bakery", 'restaurant_id': '41570001'}
{'borough': 'Manhattan', 'cuisine': 'Bakery', 'grades': [{'score': 8}, {'score': 2}, {'score': 8}], 'name': "Billy'S Bakery", 'restaurant_id': '41658998'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 8}, {'score': 12}, {'score': 10}], 'name': "Bill'S", 'restaurant_id': 
'41693376'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 12}, {'score': 12}], 'name': "Bill'S Bar And Burger Downtown", 'restaurant_id': '50000726'}
{'borough': 'Brooklyn', 'cuisine': 'Pizza', 'grades': [{'score': 11}], 'name': "Billy'S Pizza Pasta", 'restaurant_id': '50010952'}
{'borough': 'Brooklyn', 'cuisine': 'Not Listed/Not Applicable', 'grades': [{'score': 6}], 'name': 'Billet And Bellows', 'restaurant_id': '50016120'}
{'borough': 'Bronx', 'cuisine': 'American ', 'grades': [{'score': 30}, {'score': 29}, {'score': 33}, {'score': 10}, {'score': 51}], 'name': 
"Billy'S Sport Bar Restaurant & Lounge", 'restaurant_id': '40624470'}
{'borough': 'Queens', 'cuisine': 'American ', 'grades': [{'score': 12}, {'score': 12}, {'score': 16}, {'score': 15}, {'score': 19}, {'score': 11}], 'name': 'Billiard Company', 'restaurant_id': '40717559'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 12}, {'score': 2}, {'score': 13}, {'score': 10}, {'score': 11}, {'score': 14}], 'name': 'Billymarks West', 'restaurant_id': '40785565'}
{'borough': 'Queens', 'cuisine': 'American ', 'grades': [{'score': 7}, {'score': 13}, {'score': 12}, {'score': 9}, {'score': 13}], 'name': "Bill'S Restaurant", 'restaurant_id': '40868248'}
{'borough': 'Brooklyn', 'cuisine': 'American ', 'grades': [{'score': 7}, {'score': 12}, {'score': 9}], 'name': 'Billiard Club', 'restaurant_id': '41013850'}
{'borough': 'Brooklyn', 'cuisine': 'American ', 'grades': [{'score': 2}, {'score': 10}, {'score': 25}, {'score': 12}, {'score': 12}], 'name': "Bill'S Bar", 'restaurant_id': '41089835'}
{'borough': 'Queens', 'cuisine': 'American ', 'grades': [{'score': 4}, {'score': 2}, {'score': 8}, {'score': 9}], 'name': 'Billiard Room', 'restaurant_id': '41150814'}
{'borough': 'Manhattan', 'cuisine': 'Soul Food', 'grades': [{'score': 12}, {'score': 17}, {'score': 11}], 'name': "Billie'S Black Bar Lounge And Restaurant", 'restaurant_id': '41188374'}
{'borough': 'Manhattan', 'cuisine': 'Bakery', 'grades': [{'score': 9}, {'score': 12}, {'score': 12}, {'score': 10}], 'name': "Billy'S Bakery", 'restaurant_id': '41421237'}
{'borough': 'Manhattan', 'cuisine': 'Hamburgers', 'grades': [{'score': 4}, {'score': 11}, {'score': 12}, {'score': 9}], 'name': "Bill'S Bar 
& Burgers", 'restaurant_id': '41444224'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 12}, {'score': 12}, {'score': 12}, {'score': 10}], 'name': 'Billiards', 'restaurant_id': '41447357'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 10}, {'score': 3}, {'score': 9}, {'score': 7}], 'name': "Bill'S Bar & 
Burger Rockefeller Center", 'restaurant_id': '41509909'}
{'borough': 'Manhattan', 'cuisine': 'Bakery', 'grades': [{'score': 9}, {'score': 13}, {'score': 8}, {'score': 7}, {'score': 31}], 'name': "Billy'S Bakery", 'restaurant_id': '41570001'}
{'borough': 'Manhattan', 'cuisine': 'Bakery', 'grades': [{'score': 8}, {'score': 2}, {'score': 8}], 'name': "Billy'S Bakery", 'restaurant_id': '41658998'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 8}, {'score': 12}, {'score': 10}], 'name': "Bill'S", 'restaurant_id': 
'41693376'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 12}, {'score': 12}], 'name': "Bill'S Bar And Burger Downtown", 'restaurant_id': '50000726'}
{'borough': 'Brooklyn', 'cuisine': 'Pizza', 'grades': [{'score': 11}], 'name': "Billy'S Pizza Pasta", 'restaurant_id': '50010952'}
{'borough': 'Brooklyn', 'cuisine': 'Not Listed/Not Applicable', 'grades': [{'score': 6}], 'name': 'Billet And Bellows', 'restaurant_id': '50016120'}
{'borough': 'Bronx', 'cuisine': 'American ', 'grades': [{'score': 30}, {'score': 29}, {'score': 33}, {'score': 10}, {'score': 51}], 'name': 
"Billy'S Sport Bar Restaurant & Lounge", 'restaurant_id': '40624470'}
{'borough': 'Queens', 'cuisine': 'American ', 'grades': [{'score': 12}, {'score': 12}, {'score': 16}, {'score': 15}, {'score': 19}, {'score': 11}], 'name': 'Billiard Company', 'restaurant_id': '40717559'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 12}, {'score': 2}, {'score': 13}, {'score': 10}, {'score': 11}, {'score': 14}], 'name': 'Billymarks West', 'restaurant_id': '40785565'}
{'borough': 'Queens', 'cuisine': 'American ', 'grades': [{'score': 7}, {'score': 13}, {'score': 12}, {'score': 9}, {'score': 13}], 'name': "Bill'S Restaurant", 'restaurant_id': '40868248'}
{'borough': 'Brooklyn', 'cuisine': 'American ', 'grades': [{'score': 7}, {'score': 12}, {'score': 9}], 'name': 'Billiard Club', 'restaurant_id': '41013850'}
{'borough': 'Brooklyn', 'cuisine': 'American ', 'grades': [{'score': 2}, {'score': 10}, {'score': 25}, {'score': 12}, {'score': 12}], 'name': "Bill'S Bar", 'restaurant_id': '41089835'}
{'borough': 'Queens', 'cuisine': 'American ', 'grades': [{'score': 4}, {'score': 2}, {'score': 8}, {'score': 9}], 'name': 'Billiard Room', 'restaurant_id': '41150814'}
{'borough': 'Manhattan', 'cuisine': 'Soul Food', 'grades': [{'score': 12}, {'score': 17}, {'score': 11}], 'name': "Billie'S Black Bar Lounge And Restaurant", 'restaurant_id': '41188374'}
{'borough': 'Manhattan', 'cuisine': 'Bakery', 'grades': [{'score': 9}, {'score': 12}, {'score': 12}, {'score': 10}], 'name': "Billy'S Bakery", 'restaurant_id': '41421237'}
{'borough': 'Manhattan', 'cuisine': 'Hamburgers', 'grades': [{'score': 4}, {'score': 11}, {'score': 12}, {'score': 9}], 'name': "Bill'S Bar 
& Burgers", 'restaurant_id': '41444224'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 12}, {'score': 12}, {'score': 12}, {'score': 10}], 'name': 'Billiards', 'restaurant_id': '41447357'}
{'borough': 'Manhattan', 'cuisine': 'American ', 'grades': [{'score': 10}, {'score': 3}, {'score': 9}, {'score': 7}], 'name': "Bill'S Bar & 
Burger Rockefeller Center", 'restaurant_id': '41509909'}
{'borough': 'Manhattan', 'cuisine': 'Bakery', 'grades': [{'score': 9}, {'score': 13}, {'score': 8}, {'score': 7}, {'score': 31}], 'name': "Billy'S Bakery", 'restaurant_id': '41570001'}
{'borough': 'Manhattan', 'cuisine': 'Bakery', 'grades': [{'score': 8}, {'score': 2}, {'score': 8}], 'name': "Billy'S Bakery", 'restaurant_id': '41658998'}
****************************************************************************************************

`````````
## 11). 

`````````
****************************************************************************************************
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 7}, {'score': 5}, {'score': 11}, {'score': 2}], 'name': 'Mughlai Restaurant', 'restaurant_id': '40370243'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 10}, {'score': 24}, {'score': 11}, {'score': 9}, {'score': 13}, {'score': 28}], 'name': 'Agra Restaurant', 'restaurant_id': '40375376'}
{'borough': 'Queens', 'cuisine': 'Indian', 'grades': [{'score': 4}, {'score': 8}, {'score': 12}, {'score': 13}], 'name': 'Annam Braham Restaurant', 'restaurant_id': '40380520'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 5}, {'score': 8}, {'score': 12}, {'score': 2}, {'score': 9}, {'score': 92}, {'score': 41}], 'name': 'Gandhi', 'restaurant_id': '40381295'}
{'borough': 'Brooklyn', 'cuisine': 'Indian', 'grades': [{'score': 15}, {'score': 9}, {'score': 16}, {'score': 13}, {'score': 6}, {'score': 12}], 'name': 'India Passage Restaurant', 'restaurant_id': '40384479'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 12}, {'score': 9}, {'score': 13}, {'score': 12}], 'name': 'Haveli', 'restaurant_id': '40390209'}
{'borough': 'Staten Island', 'cuisine': 'Indian', 'grades': [{'score': 4}, {'score': 10}, {'score': 13}, {'score': 12}], 'name': 'Taste Of India Ii Restaurant', 'restaurant_id': '40390536'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 9}, {'score': 10}, {'score': 5}, {'score': 13}, {'score': 11}, {'score': 
15}], 'name': 'Bombay Masala', 'restaurant_id': '40394066'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 11}, {'score': 6}, {'score': 11}, {'score': 21}, {'score': 15}], 'name': 
'Indigo Indian Cuisine', 'restaurant_id': '40395748'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 12}, {'score': 15}, {'score': 12}, {'score': 19}, {'score': 26}, {'score': 13}, {'score': 37}], 'name': 'Curry In A Hurry', 'restaurant_id': '40398434'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 15}, {'score': 13}, {'score': 13}, {'score': 5}, {'score': 11}, {'score': 8}], 'name': 'Bangal Curry', 'restaurant_id': '40401972'}
{'borough': 'Queens', 'cuisine': 'Indian', 'grades': [{'score': 27}, {'score': 5}, {'score': 2}], 'name': 'Air India Lounge', 'restaurant_id': '40403419'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 8}, {'score': 0}, {'score': 3}, {'score': 4}, {'score': 18}], 'name': 'Vatan', 'restaurant_id': '40513757'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 9}, {'score': 13}, {'score': 7}, {'score': 2}, {'score': 15}], 'name': 'Madras Mahal', 'restaurant_id': '40519978'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 2}, {'score': 0}, {'score': 4}, {'score': 4}], 'name': 'Diwan-E-Khaas', 'restaurant_id': '40527369'}
{'borough': 'Queens', 'cuisine': 'Indian', 'grades': [{'score': 5}, {'score': 3}, {'score': 7}], 'name': 'Khyber Restaurant', 'restaurant_id': '40530409'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 10}, {'score': 12}, {'score': 12}, {'score': 12}], 'name': 'Ajanta India', 'restaurant_id': '40534837'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 12}, {'score': 20}, {'score': 7}, {'score': 4}, {'score': 12}], 'name': 'Raj Mahal Indian Restaurant', 'restaurant_id': '40534870'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 13}, {'score': 6}, {'score': 9}, {'score': 11}], 'name': 'Pongal Indian Cuisine', 'restaurant_id': '40544107'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 12}, {'score': 13}, {'score': 12}, {'score': 13}], 'name': 'Kismat Indian Cuisine', 'restaurant_id': '40557912'}
{'borough': 'Queens', 'cuisine': 'Indian', 'grades': [{'score': 24}, {'score': 12}, {'score': 11}, {'score': 13}, {'score': 49}, {'score': 16}, {'score': 5}], 'name': 'Santoor Indian Restaurant', 'restaurant_id': '40571663'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 2}, {'score': 3}, {'score': 10}, {'score': 4}], 'name': 'Diwan-E- Khaas', 'restaurant_id': '40598366'}
{'borough': 'Queens', 'cuisine': 'Indian', 'grades': [{'score': 11}, {'score': 8}, {'score': 9}, {'score': 10}], 'name': 'Aladdin', 'restaurant_id': '40601254'}
{'borough': 'Queens', 'cuisine': 'Indian', 'grades': [{'score': 12}, {'score': 7}, {'score': 7}, {'score': 11}], 'name': 'Mehak', 'restaurant_id': '40615240'}
{'borough': 'Queens', 'cuisine': 'Indian', 'grades': [{'score': 16}, {'score': 17}, {'score': 19}, {'score': 0}, {'score': 22}, {'score': 23}], 'name': 'Jackson Diner Indian Cuisine', 'restaurant_id': '40647953'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 5}, {'score': 11}, {'score': 10}, {'score': 17}], 'name': 'Ayurveda Cafe', 'restaurant_id': '40666541'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 9}, {'score': 12}, {'score': 12}, {'score': 9}, {'score': 27}, {'score': 
13}, {'score': 25}], 'name': 'Minar Indian Restaurant', 'restaurant_id': '40672926'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 9}, {'score': 9}, {'score': 12}, {'score': 12}, {'score': 14}, {'score': 
10}], 'name': 'Ghandi Cafe', 'restaurant_id': '40703670'}
{'borough': 'Queens', 'cuisine': 'Indian', 'grades': [{'score': 3}, {'score': 11}, {'score': 19}, {'score': 9}, {'score': 9}, {'score': 11}], 'name': 'Dosa Hutt', 'restaurant_id': '40718547'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 13}, {'score': 36}, {'score': 12}, {'score': 13}], 'name': 'Sapphire Indian Cuisine', 'restaurant_id': '40722258'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 12}, {'score': 8}, {'score': 11}, {'score': 12}, {'score': 12}], 'name': 
'Utsav Festive India Restaurant', 'restaurant_id': '40727750'}
{'borough': 'Queens', 'cuisine': 'Indian', 'grades': [{'score': 10}, {'score': 12}, {'score': 9}, {'score': 13}, {'score': 30}], 'name': 'Maurya Restaurant', 'restaurant_id': '40754126'}
{'borough': 'Brooklyn', 'cuisine': 'Indian', 'grades': [{'score': 5}, {'score': 11}, {'score': 7}, {'score': 8}, {'score': 10}], 'name': 'Taj Mahal Indian Restaurant', 'restaurant_id': '40756209'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 5}, {'score': 7}, {'score': 9}, {'score': 2}], 'name': 'Taj Cafe', 'restaurant_id': '40793198'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 9}, {'score': 12}, {'score': 11}, {'score': 10}, {'score': 10}, {'score': 16}], 'name': 'Cafe Spice', 'restaurant_id': '40793607'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 7}, {'score': 7}, {'score': 8}, {'score': 12}], 'name': 'Hampton Chutney 
Company', 'restaurant_id': '40802900'}
{'borough': 'Queens', 'cuisine': 'Indian', 'grades': [{'score': 22}, {'score': 10}, {'score': 7}, {'score': 12}, {'score': 10}, {'score': 13}], 'name': 'Al-Mehran Restaurant', 'restaurant_id': '40810032'}
{'borough': 'Queens', 'cuisine': 'Indian', 'grades': [{'score': 12}, {'score': 10}, {'score': 15}, {'score': 7}, {'score': 13}, {'score': 19}], 'name': 'Indian Taj', 'restaurant_id': '40827157'}
{'borough': 'Queens', 'cuisine': 'Indian', 'grades': [{'score': 5}, {'score': 10}, {'score': 10}, {'score': 13}, {'score': 9}], 'name': 'Gandhi Indian Cuisine', 'restaurant_id': '40827726'}
{'borough': 'Queens', 'cuisine': 'Indian', 'grades': [{'score': 13}, {'score': 12}, {'score': 5}, {'score': 17}, {'score': 23}], 'name': 'Devasthanam Canteen', 'restaurant_id': '40835821'}
{'borough': 'Queens', 'cuisine': 'Indian', 'grades': [{'score': 18}, {'score': 13}, {'score': 5}, {'score': 7}, {'score': 33}, {'score': 12}, {'score': 13}], 'name': 'Maharaja Quality Sweets', 'restaurant_id': '40836314'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 7}, {'score': 9}, {'score': 12}, {'score': 60}, {'score': 9}], 'name': 'Minar Indian Restaurant', 'restaurant_id': '40871006'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 8}, {'score': 9}, {'score': 18}, {'score': 5}, {'score': 10}, {'score': 18}], 'name': 'Amma', 'restaurant_id': '40885805'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 20}, {'score': 7}, {'score': 9}], 'name': 'The Kati Roll Company', 'restaurant_id': '40901527'}
{'borough': 'Brooklyn', 'cuisine': 'Indian', 'grades': [{'score': 11}, {'score': 12}, {'score': 7}, {'score': 22}, {'score': 45}, {'score': 
17}], 'name': 'Joy Indian Restaurant', 'restaurant_id': '40928416'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 12}, {'score': 25}, {'score': 22}, {'score': 14}, {'score': 3}, {'score': 11}], 'name': "Baluchi'S", 'restaurant_id': '40936006'}
{'borough': 'Brooklyn', 'cuisine': 'Indian', 'grades': [{'score': 11}, {'score': 11}, {'score': 27}, {'score': 9}, {'score': 12}, {'score': 
22}], 'name': 'Britain Indian Restaurant', 'restaurant_id': '40944839'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 10}, {'score': 16}, {'score': 8}, {'score': 2}, {'score': 5}, {'score': 11}, {'score': 13}], 'name': 'Joy Curry & Tandoor', 'restaurant_id': '40946298'}
{'borough': 'Queens', 'cuisine': 'Indian', 'grades': [{'score': 10}, {'score': 12}, {'score': 12}, {'score': 9}, {'score': 2}, {'score': 11}], 'name': 'World Fair Marina Restaurant & Banquet', 'restaurant_id': '40947943'}
{'borough': 'Manhattan', 'cuisine': 'Indian', 'grades': [{'score': 14}, {'score': 18}, {'score': 26}, {'score': 2}, {'score': 19}, {'score': 10}], 'name': "Baluchi'S", 'restaurant_id': '40978503'}
****************************************************************************************************

`````````
## 12). Write a MongoDB query to find the restaurant Id, name, borough, cuisines, and score for those restaurants which contain 'bi' as last three letters for its name.
`````````
****************************************************************************************************
****************************************************************************************************
{'borough': 'Queens', 'cuisine': 'Chinese', 'grades': [{'score': 10}, {'score': 12}, {'score': 10}, {'score': 12}], 'name': 'Mr Wasabi', 'restaurant_id': '40997900'}
{'borough': 'Queens', 'cuisine': 'Japanese', 'grades': [{'score': 7}, {'score': 13}, {'score': 9}], 'name': 'Gowasabi', 'restaurant_id': '41431748'}
{'borough': 'Brooklyn', 'cuisine': 'Japanese', 'grades': [{'score': 13}, {'score': 18}, {'score': 2}, {'score': 31}], 'name': 'Wasabi', 'restaurant_id': '50002381'}
{'borough': 'Brooklyn', 'cuisine': 'Korean', 'grades': [{'score': 11}, {'score': 11}], 'name': 'Little Dokebi', 'restaurant_id': '50003236'}{'borough': 'Manhattan', 'cuisine': 'Japanese', 'grades': [{'score': 9}], 'name': 'Hanabi', 'restaurant_id': '50010310'}
{'borough': 'Manhattan', 'cuisine': 'Café/Coffee/Tea', 'grades': [{'score': 56}], 'name': 'Matcha Cafe Wabi', 'restaurant_id': '50016721'}  
{'borough': 'Manhattan', 'cuisine': 'Other', 'grades': [], 'name': 'Kuro-Obi', 'restaurant_id': '50018850'}
{'borough': 'Queens', 'cuisine': 'Chinese', 'grades': [{'score': 10}, {'score': 12}, {'score': 10}, {'score': 12}], 'name': 'Mr Wasabi', 'restaurant_id': '40997900'}
{'borough': 'Queens', 'cuisine': 'Japanese', 'grades': [{'score': 7}, {'score': 13}, {'score': 9}], 'name': 'Gowasabi', 'restaurant_id': '41431748'}
{'borough': 'Brooklyn', 'cuisine': 'Japanese', 'grades': [{'score': 13}, {'score': 18}, {'score': 2}, {'score': 31}], 'name': 'Wasabi', 'restaurant_id': '50002381'}
{'borough': 'Brooklyn', 'cuisine': 'Korean', 'grades': [{'score': 11}, {'score': 11}], 'name': 'Little Dokebi', 'restaurant_id': '50003236'}{'borough': 'Manhattan', 'cuisine': 'Japanese', 'grades': [{'score': 9}], 'name': 'Hanabi', 'restaurant_id': '50010310'}
{'borough': 'Manhattan', 'cuisine': 'Café/Coffee/Tea', 'grades': [{'score': 56}], 'name': 'Matcha Cafe Wabi', 'restaurant_id': '50016721'}  
{'borough': 'Manhattan', 'cuisine': 'Other', 'grades': [], 'name': 'Kuro-Obi', 'restaurant_id': '50018850'}
{'borough': 'Queens', 'cuisine': 'Chinese', 'grades': [{'score': 10}, {'score': 12}, {'score': 10}, {'score': 12}], 'name': 'Mr Wasabi', 'restaurant_id': '40997900'}
{'borough': 'Queens', 'cuisine': 'Japanese', 'grades': [{'score': 7}, {'score': 13}, {'score': 9}], 'name': 'Gowasabi', 'restaurant_id': '41431748'}
{'borough': 'Brooklyn', 'cuisine': 'Japanese', 'grades': [{'score': 13}, {'score': 18}, {'score': 2}, {'score': 31}], 'name': 'Wasabi', 'restaurant_id': '50002381'}
{'borough': 'Brooklyn', 'cuisine': 'Korean', 'grades': [{'score': 11}, {'score': 11}], 'name': 'Little Dokebi', 'restaurant_id': '50003236'}{'borough': 'Manhattan', 'cuisine': 'Japanese', 'grades': [{'score': 9}], 'name': 'Hanabi', 'restaurant_id': '50010310'}
{'borough': 'Manhattan', 'cuisine': 'Café/Coffee/Tea', 'grades': [{'score': 56}], 'name': 'Matcha Cafe Wabi', 'restaurant_id': '50016721'}  
{'borough': 'Manhattan', 'cuisine': 'Other', 'grades': [], 'name': 'Kuro-Obi', 'restaurant_id': '50018850'}
{'borough': 'Queens', 'cuisine': 'Chinese', 'grades': [{'score': 10}, {'score': 12}, {'score': 10}, {'score': 12}], 'name': 'Mr Wasabi', 'restaurant_id': '40997900'}
{'borough': 'Queens', 'cuisine': 'Japanese', 'grades': [{'score': 7}, {'score': 13}, {'score': 9}], 'name': 'Gowasabi', 'restaurant_id': '41431748'}
{'borough': 'Brooklyn', 'cuisine': 'Japanese', 'grades': [{'score': 13}, {'score': 18}, {'score': 2}, {'score': 31}], 'name': 'Wasabi', 'restaurant_id': '50002381'}
{'borough': 'Brooklyn', 'cuisine': 'Korean', 'grades': [{'score': 11}, {'score': 11}], 'name': 'Little Dokebi', 'restaurant_id': '50003236'}{'borough': 'Manhattan', 'cuisine': 'Japanese', 'grades': [{'score': 9}], 'name': 'Hanabi', 'restaurant_id': '50010310'}
{'borough': 'Manhattan', 'cuisine': 'Café/Coffee/Tea', 'grades': [{'score': 56}], 'name': 'Matcha Cafe Wabi', 'restaurant_id': '50016721'}  
{'borough': 'Manhattan', 'cuisine': 'Other', 'grades': [], 'name': 'Kuro-Obi', 'restaurant_id': '50018850'}
{'borough': 'Queens', 'cuisine': 'Chinese', 'grades': [{'score': 10}, {'score': 12}, {'score': 10}, {'score': 12}], 'name': 'Mr Wasabi', 'restaurant_id': '40997900'}
{'borough': 'Queens', 'cuisine': 'Japanese', 'grades': [{'score': 7}, {'score': 13}, {'score': 9}], 'name': 'Gowasabi', 'restaurant_id': '41431748'}
{'borough': 'Brooklyn', 'cuisine': 'Japanese', 'grades': [{'score': 13}, {'score': 18}, {'score': 2}, {'score': 31}], 'name': 'Wasabi', 'restaurant_id': '50002381'}
{'borough': 'Brooklyn', 'cuisine': 'Korean', 'grades': [{'score': 11}, {'score': 11}], 'name': 'Little Dokebi', 'restaurant_id': '50003236'}{'borough': 'Manhattan', 'cuisine': 'Japanese', 'grades': [{'score': 9}], 'name': 'Hanabi', 'restaurant_id': '50010310'}
{'borough': 'Manhattan', 'cuisine': 'Café/Coffee/Tea', 'grades': [{'score': 56}], 'name': 'Matcha Cafe Wabi', 'restaurant_id': '50016721'}  
{'borough': 'Manhattan', 'cuisine': 'Other', 'grades': [], 'name': 'Kuro-Obi', 'restaurant_id': '50018850'}
{'borough': 'Queens', 'cuisine': 'Chinese', 'grades': [{'score': 10}, {'score': 12}, {'score': 10}, {'score': 12}], 'name': 'Mr Wasabi', 'restaurant_id': '40997900'}
{'borough': 'Queens', 'cuisine': 'Japanese', 'grades': [{'score': 7}, {'score': 13}, {'score': 9}], 'name': 'Gowasabi', 'restaurant_id': '41431748'}
{'borough': 'Brooklyn', 'cuisine': 'Japanese', 'grades': [{'score': 13}, {'score': 18}, {'score': 2}, {'score': 31}], 'name': 'Wasabi', 'restaurant_id': '50002381'}
{'borough': 'Brooklyn', 'cuisine': 'Korean', 'grades': [{'score': 11}, {'score': 11}], 'name': 'Little Dokebi', 'restaurant_id': '50003236'}{'borough': 'Manhattan', 'cuisine': 'Japanese', 'grades': [{'score': 9}], 'name': 'Hanabi', 'restaurant_id': '50010310'}
{'borough': 'Manhattan', 'cuisine': 'Café/Coffee/Tea', 'grades': [{'score': 56}], 'name': 'Matcha Cafe Wabi', 'restaurant_id': '50016721'}  
{'borough': 'Manhattan', 'cuisine': 'Other', 'grades': [], 'name': 'Kuro-Obi', 'restaurant_id': '50018850'}
{'borough': 'Queens', 'cuisine': 'Chinese', 'grades': [{'score': 10}, {'score': 12}, {'score': 10}, {'score': 12}], 'name': 'Mr Wasabi', 'restaurant_id': '40997900'}
{'borough': 'Queens', 'cuisine': 'Japanese', 'grades': [{'score': 7}, {'score': 13}, {'score': 9}], 'name': 'Gowasabi', 'restaurant_id': '41431748'}
{'borough': 'Brooklyn', 'cuisine': 'Japanese', 'grades': [{'score': 13}, {'score': 18}, {'score': 2}, {'score': 31}], 'name': 'Wasabi', 'restaurant_id': '50002381'}
{'borough': 'Brooklyn', 'cuisine': 'Korean', 'grades': [{'score': 11}, {'score': 11}], 'name': 'Little Dokebi', 'restaurant_id': '50003236'}{'borough': 'Manhattan', 'cuisine': 'Japanese', 'grades': [{'score': 9}], 'name': 'Hanabi', 'restaurant_id': '50010310'}
{'borough': 'Manhattan', 'cuisine': 'Café/Coffee/Tea', 'grades': [{'score': 56}], 'name': 'Matcha Cafe Wabi', 'restaurant_id': '50016721'}  
{'borough': 'Manhattan', 'cuisine': 'Other', 'grades': [], 'name': 'Kuro-Obi', 'restaurant_id': '50018850'}
{'borough': 'Queens', 'cuisine': 'Chinese', 'grades': [{'score': 10}, {'score': 12}, {'score': 10}, {'score': 12}], 'name': 'Mr Wasabi', 'restaurant_id': '40997900'}
****************************************************************************************************
`````````
## 14).Write a query to show all the restaurant Id, name, borough, cuisines, and score for those restaurants which contain 'il' anywhere in its name.
