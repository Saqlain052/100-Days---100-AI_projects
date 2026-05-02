from transformers import pipeline

print (" Model Loading")

spam_classifier = pipeline('text-classification', model = "mrm8488/bert-tiny-finetuned-sms-spam-detection")
print("Model Loaded")

def spam_check(text):
  result = spam_classifier(text)[0]
  label = result['label']
  score = result['score']

  if label =="Label_1":
    status = "Spam"
  else:
    status = "Not Spam"
  print(f'Result: {status}')
  print("_" * 20)
  print(f'Confidence Score:{score}')
  return status , score

multiple_emails = [
    # SPAM emails
    "WINNER!! You have been selected for $1000 cash prize. Call now!",
    "FREE entry in 2 a weekly comp to win FA Cup Final tickets!",
    "Urgent: Your account will be suspended. Click here to verify.",

    # Normal emails
    "Hey, are you coming to the meeting tomorrow at 3pm?",
    "Please find attached the report you requested.",
    "Thanks for your order! Your package will arrive in 2-3 days."
]

for i in multiple_emails:
  final_result = spam_check(i)
  print(final_result)

my_email = input('Enter Your email:')
spam_check(my_email)
