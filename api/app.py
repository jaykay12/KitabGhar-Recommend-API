from flask import Flask, request, jsonify
import recommender


popRecomSales = recommender.PopularityRecommenderSales()
popRecomRatings = recommender.PopularityRecommenderRatings()
itemCFRecom = recommender.ItemSimilarityRecommender()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flask App is Running!"


@app.route("/recommendations/sales")
def getSalesRecommendations():
	response = {}
	try:
			recommendations = popRecomSales.getRecommendations()
			response["recommendations"] = recommendations
			response["message"] = "Retrieved Recommendations based on top sales"
			response["success"] = True
	except Exception as e:
		response["success"] = False
		response["message"] = "No Recommendations Found based on top sales!"
	finally:
		return jsonify(**response)


@app.route("/recommendations/ratings")
def getRatingsRecommendations():
	response = {}
	try:
			recommendations = popRecomRatings.getRecommendations()
			response["recommendations"] = recommendations
			response["message"] = "Retrieved Recommendations based on top ratings"
			response["success"] = True
	except Exception as e:
		response["success"] = False
		response["message"] = "No Recommendations Found based on top ratings!"
	finally:
		return jsonify(**response)

@app.route("/recommendations/itembased/<string:userid>")
def getItemBasedRecommendations(userid):
	response = {}
	try:
			recommendations = itemCFRecom.getRecommendations(userid)
			response["recommendations"] = recommendations
			response["message"] = "Retrieved Recommendations for the userid: "+str(userid)
			response["success"] = True
	except Exception as e:
		response["success"] = False
		response["message"] = "No Recommendations Found for the userid: "+str(userid)
	finally:
		return jsonify(**response)


if __name__ =='__main__':
	app.run(debug=True)
