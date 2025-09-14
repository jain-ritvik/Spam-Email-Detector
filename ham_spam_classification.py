# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/ritvi/Downloads/archive/spam_ham_dataset.csv")
# print(df.head())
print(df['label'].value_counts())

plt.figure()
df['label'].value_counts().plot(kind='bar', color=['green', 'red'])
plt.title('Ham vs Spam')
plt.xlabel("Label")
plt.ylabel('Count')
plt.show()

total_mails = len(df)
total_spam = (df['label'] == 'spam').sum()
total_ham = (df['label'] == 'ham').sum()

ham_percentage = total_ham / total_mails * 100
spam_percentage = total_spam / total_mails * 100
total_percentage = (total_ham + total_spam) / total_mails * 100

summary_table = pd.DataFrame({'Label':['Ham', 'Spam', 'Total'],
                              'Count':[total_ham, total_spam, total_mails],
                              'Percentage':[f"{ham_percentage:.2f}%", f"{spam_percentage:.2f}%", f"{total_percentage:.2f}%"]
                              })
print(summary_table)

df['email_length']=df['text'].apply(len)
avg_spam_len = df[df['label'] == 'spam']['email_length'].mean()
avg_ham_len = df[df['label'] == 'ham']['email_length'].mean()

print(f"Average Spam Length is: {avg_spam_len:.2f} characters")
print(f"Average Ham Length is: {avg_ham_len:.2f} characters")

plt.figure()
df[df['label'] =='spam']['email_length'].plot(kind='hist', bins=100, alpha=0.5, label='spam', color='blue')
df[df['label'] =='ham']['email_length'].plot(kind='hist', bins=100, alpha=0.5, label='ham', color='red')
plt.title('Email Length')
plt.xlabel('Characters Count')
plt.ylabel('Frequency')
plt.xlim(0,10000)
plt.legend()
plt.show()
