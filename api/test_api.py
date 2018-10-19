import recommender

def test_PopularityRecommendationsSales():
	popRecomSales = recommender.PopularityRecommenderSales()
	recommendations = popRecomSales.getRecommendations()
	print(recommendations)
	assert len(recommendations) > 0

def test_PopularityRecommendationsRatings():
	popRecomRatings = recommender.PopularityRecommenderRatings()
	recommendations = popRecomRatings.getRecommendations()
	print(recommendations)
	assert len(recommendations) > 0

def test_ItemSimilarityREcommendations():
	itemCFRecom = recommender.ItemSimilarityRecommender()
	recommendations = itemCFRecom.getRecommendations('jalaz.kumar')
	print(recommendations)
	assert len(recommendations) > 0