from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from prediction_endpoint.models import Prediction
from prediction_endpoint.ClientPrediction import ClientPrediction

def index(request):

	lat1 = request.GET.get('lat1')
	lat2 = request.GET.get('lat2')
	long1 = request.GET.get('long1')
	long2 = request.GET.get('long2')

	# query for predictions within the bounding box
	preds = Prediction.objects.filter(latitude__range=(lat1, lat2),
							          longitude__range=(long1, long2))

	# convert all predictions into Prediction objects
	return_list = [ClientPrediction(pred.latitude,
									pred.longitude,
									pred.label) for pred in preds]
	#send list back to client
	return JsonResponse({'preds': [pred.to_dict() for pred in return_list]})
