from keras.layers import Convolution2D , MaxPooling2D , Flatten, Dense
from keras.models import Sequential
from keras.models import load_model
from keras_preprocessing.image import ImageDataGenerator
import sys

arg_list = sys.argv

flag = True
with open("/Code/" + file, 'r') as reader:

	for line in reader:
		if double(line) >= 80.0:
			flag = False
		else:
			flag = True

if flag:
	pass;
else:

	def build_model(neuron , n)
		model = Sequential()
		model.add(Convolution2D(32,3, activation='relu', input_shape=(64,64,3)))
		model.add(MaxPooling2D())
		model.add(Flatten())
		for i in range(1,n)
			model.add(Dense(units=neuron, activation='relu'))
			neuron /= 2
		model.add(Dense(units=1,activation='sigmoid'))
		model.compile(optimizer='adam', loss='binary_crossentropy',metrics = ['accuracy'] )

	build_model(arg_list[1],arg_list[0])

	
	train_datagen = ImageDataGenerator(
		rescale=1./255,
		shear_range=0.2,
		zoom_range=0.2,
		horizontal_flip=True)
	test_datagen = ImageDataGenerator(rescale=1./255)
	training_set = train_datagen.flow_from_directory(
		'/Dataset/training_set/',
		target_size=(64, 64),
		batch_size=32,
		class_mode='binary')
	test_set = test_datagen.flow_from_directory(
		'/Dataset/test_set/',
		target_size=(64, 64),
		batch_size=32,
		class_mode='binary')
	model.fit(
		training_set,
		steps_per_epoch=8000,
		epochs=1,
		validation_data=test_set,
		validation_steps=800)

	model.save('/Model/cat_and_dog.h5')
	file = open("text.txt", "w") 
	file.write(str(model(test_set)[1])) 
	file.close()

