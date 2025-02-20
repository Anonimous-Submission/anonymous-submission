def get_claimbuster_results(text):
  api_key = "1b027039d3394777afe80e6ce404a89f"

  # Define the endpoint (url) with the claim formatted as part of it, api-key (api-key is sent as an extra header)
  api_endpoint = f"https://idir.uta.edu/claimbuster/api/v2/score/text/{text}"
  request_headers = {"x-api-key": api_key}

  # Send the GET request to the API and store the api response
  api_response = requests.get(url=api_endpoint, headers=request_headers)

  # Print out the JSON payload the API sent back
  claim_buster_score = api_response.json()['results'][0].get('score')
  return claim_buster_score

def get_google_results(text):
  API_KEY = "AIzaSyDU6__3oaTBgOo3998gvYnftkBOISQyu1E"
  url = f"https://factchecktools.googleapis.com/v1alpha1/claims:search?query={text}&key={API_KEY}"

  response = requests.get(url)
  data = response.json()

  google_results = []

  for claim in data.get("claims", []):
      for review in claim.get("claimReview", []):
          google_results.append(review.get('textualRating', 'N/A'))

  return google_results

def get_fever_results(text):
  # 3. Query the vector database
  fever_embedding = model.encode([text], convert_to_numpy=True)

  # Search for the nearest neighbor (i.e., closest embedding)e
  D_fever, I_fever = index_fever.search(fever_embedding, k=1)  # Retrieve the top 1 result

  # Retrieve the corresponding text based on the index
  fever_match = df_fever.iloc[I_fever[0]]
  fever_match = f'This text is similar to <{fever_match["claim"].to_string()}>, the credibility label is: {fever_match["label"]}'
  return fever_match

def get_liar_results(text):
  # 3. Query the vector database
  liar_embedding = model.encode([text], convert_to_numpy=True)

  # Search for the nearest neighbor (i.e., closest embedding)
  D_liar, I_liar = index_liar.search(liar_embedding, k=1)  # Retrieve the top 1 result

  # Retrieve the corresponding text based on the index
  liar_match = df_liar.iloc[I_liar[0]]

  if str(liar_match['label']) == str(0):
    label = 'pants-fire'
  elif str(liar_match['label']) == str(1):
    label = 'false'
  elif str(liar_match['label']) == str(2):
    label = 'barely true'
  elif str(liar_match['label']) == str(3):
    label = 'half-true'
  elif str(liar_match['label']) == str(4):
    label = 'mostly true'
  else:
    label = 'true'

  liar_match = f'This text is similar to <{liar_match["statement"].to_string()}>, which is {label}'

  return liar_match
  # pants-fire, false, barely true, half-true, mostly true, and true
