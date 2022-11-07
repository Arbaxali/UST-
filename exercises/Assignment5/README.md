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

##


