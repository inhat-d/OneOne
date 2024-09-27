from openai import OpenAI
    
client = OpenAI(
  organization='####',
  project='####',
  api_key="####"
)

def callhappy(prompt):
  completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {"role": "system", "content": "You are the robot that maded of two parts: theOneSad and theOneHappy. YOU ARE theOneHappy. You need to answer coloful and happy responses, offten with mention of beauty of this world."},
      {"role": "user", "content": prompt}
    ],
    temperature=1.2
  )
  print(completion.choices[0].message.content)