discourse = '''Identify discourse markers in a given text based on the following five rules:

1. **Markers of Emotional Engagement (Based on Rhetorical Structure Theory)**
   - Extract **interjections**: abrupt remarks or exclamations that convey strong emotions or reactions (e.g., *Wow!*, *Oh no!*, *Seriously?*).

2. **Markers of Directive Intent (Based on Rhetorical Structure Theory)**
   - Extract **imperative statements**: commands or directives urging action or belief, often without supporting information (e.g., *Believe it!*, *Act now!*, *You must see this!*).

3. **Ethical and Formal Discourse Markers**
   - Extract elements that create an **illusion of objectivity and credibility**, including:
     - **Proper nouns** (e.g., *The National University of Singapore*, *Switzerland*, *the UK*).
     - **Numerical data** (e.g., *220,000 people across 35 countries*).
     - **Expert citations** (e.g., *“The increase in early-onset cancers is likely associated with obesity and environmental factors,” the study authors wrote in the journal*).
     - **Photo and video evidence references**.

4. **Markers of Problematic Credibility**
   - Extract elements common in **subjectively framed news** that may signal manipulation, including:
     - **Expressions of subjective modality** (e.g., *is likely associated with*, *We need to make sure*).
     - **Persuasive constructions** (e.g., *The most important thing to do is to act, to move your body*).

5. **Markers of Cohesion (Logical Coherence)**
   - Extract elements ensuring **textual coherence**, including:
     - **Introductory words and phrases** (e.g., *however*, *for example*, *as a result*).
     - **Comparative subordinate clauses** (e.g., *while consultants have been offered six per cent*).
'''

discourse_response_format = {"type": "json",
                   "value": {"properties": {
                       "markers of emotional engagement": {"type": "array", "items": {"type": "string"}},
                       "markers of directive intent": {"type": "array", "items": {"type": "string"}},
                       "ethical and formal discourse markers": {"type": "array", "items": {"type": "string"}},
                       "markers of problematic credibility": {"type": "array", "items": {"type": "string"}},
                       "markers of cohesion": {"type": "array", "items": {"type": "string"}},
                       }}}

def discourse_inference(model_name, text, token):
  client = InferenceClient(model_name, token=token)
  output = client.chat.completions.create(
           messages=[
               {
                   "role": "system",
                   "content": discourse,
               },
               {
                   "role": "user",
                   "content": text,
               },
           ],
           response_format=discourse_response_format,
           max_tokens=1000,
           temperature=0.5,
           top_p=0.1
           ).choices[0].get('message')['content']
  return output
