def scoring(model_name, text, token, claim_buster_score, google_results, liar_match, fever_match, discourse_results, security_analysis):
  scoring_prompt = f"""#### System Instruction:
  Evaluate the source credibility based on the provided sources
  Explain your reasoning
  ClaimBuster score: {claim_buster_score}
  Google Fact Check results: {google_results}
  LIAR database match: {liar_match}
  FEVER database match: {fever_match}
  Discourse analysis results: {discourse_results}
  Cybersecutiry analysis results: {security_analysis}
  """

  scoring_response_format = {"type": "json",
                            "value": {"properties": {
                                                      "database analysis": {"type": "string"},
                                                      "cybersecurity verdict": {"type": "string"},
                                                      "discource analysis result": {"type": "string"},
                                                      "reasoning": {"type": "string"},
                                                      "verdict": {"type": "string"},
                                                    },
                                      "required": ["database analysis", "cybersecurity verdict", "discource analysis result", "reasoning", "verdict"],}}
  client = InferenceClient(model_name, token=token)
  output = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": scoring_prompt,
                },
                {
                    "role": "user",
                    "content": text,
                },
            ],
            response_format=scoring_response_format,
            max_tokens=1000,
            temperature=0.5,
            top_p=0.1
            ).choices[0].get('message')['content']
  return output
