# photorate
Flask serves photos folder content as webserver (defiend in config json e.g C:/wedding/photos) <br />
creates 3 folders for sorting photos at 1 level up ( e.g C:/wedding/no,C:/wedding/maybe,C:/wedding/yes ) <br />
webpage with tab for each folder content and buttons that allow moving the image between the folders <br />


![Capture](https://user-images.githubusercontent.com/40518583/123522115-f6a66980-d6c3-11eb-9da0-d692917e8b02.JPG)



creating exe:
``` pyinstaller -F --add-data="templates;templates" main.py ```