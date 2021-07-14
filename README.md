# ProductRecommendation

1.	Json to CSV Convert
2.	Merge Datasets
3.	Preprocessing Data
4.	User-based Analysis
5.	Item-Based Analysis
6.	Outputs

1.	First of all, I converted dataset type from Json to CSV. With pandas, manipulating and managing data is efficient way. Also, by making csv output I read and understand dataset better.

2.	Session and product type are straightly related to each other. Session is buying process and cart of user and include all products. Productid is the primary key of the both table and by using it I merged those datasets.

3.	Preprocessing data is the key part of data science. In datasets, we shouldnt have NaN and unrelated objects to make better our accuracy. I dropped all NaNs. Also converted cart column to float “1” because for correlasion analysis, we should have an item that is make connected to product id and sessionid. For me cart is an action and this action on our dataset is buying a item. So I converted this to float and used for the analysis.

4.	 Firstly I created a customer item matrix which is a table for showing which customer bought which product. Then, applied a function to reject all NaNs and  use all entities.After all process I applied Cosine similarity to see customers relation to each other  and  who is more related and close each other. Some customers buying habits can similar and if we solve this similarity we can recommend products. So more close customers, better recommendation. After all,we can see the similarity ratio and recommend products.

5.	 Item-based is similar with user-based but this time we use relation between products. We transform the customer table and see which products bought in the same time and which one is more similar then others to each other. By using similarity function and see which 10 products are more similar.

6.	For outputs, as you mentioned on the paper I chose a product and use this similarity function and recommended products. The products which are recommended on below.

![2021-07-13](https://user-images.githubusercontent.com/32933218/125441741-900a1adf-9ffd-4bac-a640-7444e1a58dad.png)

# API 

The api has a page for cart product and after take it, function calls and return 10 recomended products to page.

![2021-07-14](https://user-images.githubusercontent.com/32933218/125624909-0d65a22d-b469-4a76-b7f5-c1ec0f172efb.png)

