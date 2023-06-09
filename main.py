from PIL import Image, ImageEnhance
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField, IntegerField, SubmitField
from flask_wtf.recaptcha import RecaptchaField

app = Flask(__name__, template_folder='C:/Users/Андрей/PycharmProjects/pythonProject4')

app.config['SECRET_KEY'] = '6LfIM34mAAAAAC44SAE6zfvxBBqXDccnutHPsDW1'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LfIM34mAAAAADZCMVpHTjzPdz6VTaKWjhKZ112t'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LfIM34mAAAAAC44SAE6zfvxBBqXDccnutHPsDW1'

def img_return(file1, file2):
    width1 = file1.width
    width2 = file2.width
    image1 = np.array(file1)
    image2 = np.array(file2)
    # Создание места для графиков и изображений
    fig = plt.figure(figsize=(14, 7))

    # Первое изображение
    p1 = fig.add_subplot(2, 2, 1)
    p1.imshow(image1)
    p1.set_title('Исходное изображение')

    # Второе изображение
    p2 = fig.add_subplot(2, 2, 2)
    p2.imshow(image2)
    p2.set_title('Изменённое изображение')


    # График распределения цветов первого изображения
    ax1 = fig.add_subplot(2, 2, 3)
    ax1.set(xlim=(0, width1), ylim=(0, 255))
    ax1.plot(np.mean(image1[:, :, 0], axis=0), 'r', label='Red')
    ax1.plot(np.mean(image1[:, :, 1], axis=0), 'g', label='Green')
    ax1.plot(np.mean(image1[:, :, 2], axis=0), 'b', label='Blue')
    ax1.set_xlabel('Ширина')
    ax1.set_ylabel('Значение цветового канала')
    ax1.set_title('Цветовые каналы')
    ax1.legend()

    # График распределения цветов второго изображения
    ax2 = fig.add_subplot(2, 2, 4)
    ax2.set(xlim=(0, width2), ylim=(0, 255))
    ax2.plot(np.mean(image2[:, :, 0], axis=0), 'r', label='Red')
    ax2.plot(np.mean(image2[:, :, 1], axis=0), 'g', label='Green')
    ax2.plot(np.mean(image2[:, :, 2], axis=0), 'b', label='Blue')
    ax2.set_xlabel('Ширина')
    ax2.set_ylabel('Значение цветового канала')
    ax2.set_title('Цветовые каналы')
    ax2.legend()

    #Вывод всего на экран
    plt.savefig('static/Graph.jpg')
    #plt.show()

def size_HUI(file, fixed_width):
    # получаем процентное соотношение
    # старой и новой ширины
    width_percent = (fixed_width / float(file.size[0]))
    # на основе предыдущего значения
    # вычисляем новую высоту
    height_size = int((float(file.size[0]) * float(width_percent)))
    # меняем размер на полученные значения
    new_image = file.resize((fixed_width, height_size))
    return new_image

class MyForm(FlaskForm):
    image = FileField('Выберите изображение')
    fixed_width = IntegerField('Выберите яркость (от 0.0 до 2.0)')
    recaptcha = RecaptchaField()
    submit = SubmitField('Применить')

@app.route('/', methods=['GET', 'POST'])
def captcha():
    form = MyForm()
    if form.validate_on_submit():
        return render_template('one.html', form=form)
    return render_template('base.html', form=form)

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['image']
        f.save('Korben.jpg')
        file = Image.open('Korben.jpg')
        fixed_width = int(request.form['fixed_width'])
        img_return(file, size_HUI(file, fixed_width))
        return render_template("index.html")

def one():
    return render_template('one.html')

def base():
    return render_template("base.html")

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.get('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'    

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000)
    
   

    
