This is an example of LLM inference based on our function:

Baseline model: 'deepseek-ai/DeepSeek-R1-Distill-Qwen-32B', result:
```
Discourse Analysis:
                    {
                      'markers of emotional engagement':
                                                          [],
                      'markers of directive intent':
                                                          ['Share a certain post of Bill Gates on Facebook and he will send you money.', 'If you click that share link, I will give you $5,000.'],
                      'ethical and formal discourse markers':
                                                          ['Bill Gates', 'Windows XP'],
                      'markers of problematic credibility':
                                                          ['I always deliver', 'I mean'],
                      'markers of cohesion':
                                                          []}
```

Baseline model: 'Qwen/QwQ-32B-Preview', result:
```
Discourse Analysis:
                    {
                      'markers of emotional engagement':
                                                          ['Hey', 'right?'],
                      'markers of directive intent':
                                                          ['click that share link', 'I will give you $5,000'],
                      'ethical and formal discourse markers':
                                                          ["As some of you may know, I'm Bill Gates", 'I always deliver', 'I mean, I brought you Windows XP'],
                      'markers of problematic credibility':
                                                          ['I will give you $5,000', 'I always deliver', 'I mean, I brought you Windows XP'],
                      'markers of cohesion':
                                                          ['As some of you may know', 'right?']}
```

Baseline model: 'mistralai/Mistral-7B-Instruct-v0.3', result:
```
Discourse Analysis:
                    {
                      'markers of emotional engagement':
                                                          ['Hey'],
                      'markers of directive intent':
                                                          ['If you click that share link'],
                      'ethical and formal discourse markers':
                                                          ['Bill Gates'],
                      'markers of problematic credibility':
                                                          ['I always deliver'],
                      'markers of cohesion':
                                                          ['I mean, I brought you Windows XP, right?']}
```
