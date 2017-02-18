#import pandas and numpy
import pandas as pd
import numpy as np

#create dataframe with some random data
df = pd.DataFrame(np.random.rand(10, 2) * 10, columns=['Price', 'Qty'])

#add a column with random string values that would need to have dummy variables created for them
df['City'] = [np.random.choice(('Chicago', 'Boston', 'New York')) for i in range(df.shape[0])]

#create dummy variables for the column
dummies = pd.get_dummies(df['City'])

#drop the original column
df = df.drop('City', axis=1)

#add dummy variables
df = df.join(dummies)

print(df)