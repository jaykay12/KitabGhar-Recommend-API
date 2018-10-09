import recommender

popRecomSales = recommender.PopularityRecommenderSales()
recommendations = popRecomSales.getRecommendations()
print("# - - - - - - Test Cases - - - - - #")
print(recommendations)
print("\n\n\n")

popRecomRatings = recommender.PopularityRecommenderRatings()
recommendations = popRecomRatings.getRecommendations()
print("# - - - - - - Test Cases - - - - - #")
print(recommendations)
print("\n\n\n")

itemCFRecom = recommender.ItemSimilarityRecommender()
recommendations = itemCFRecom.getRecommendations('jalaz.kumar')
print("# - - - - - - Test Cases - - - - - #")
print(recommendations)
print("\n\n\n")
