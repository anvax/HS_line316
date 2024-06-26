# Hs line 316 Система управления 
 
## Авторы 
 
Худобин Андрей

Гайфулин Тимур

Пасечко Иван

Вязовский Владислав 
 
Руководитель: 
Куклин Егор Вадимович 
 
# Описание проекта 
 
Проект заключается в реализации программного обеспечения упаковочной линии, расположенной в 316 аудитории. 
 
Установка представляет собой набор нескольких объектов, которые выполняют свою задачу в процессе работы линии: вращающейся платформы, гриппера, упаковочной линии, сортировочной линии. 
 
## Начало работы 
 
Перед запуском необходимо установить библиотеку opcua 
 
    pip install opcua 
 
Либо воспользоваться [docker контейнером](https://hub.docker.com/repository/docker/spynch/hsline316/general )  
([Если жалуется на регион](https://huecker.io/))

    docker pull spynch/hsline316

Реализация модели клиент-сервер OPC UA позволит интегрировать лабораторную станцию по мехатронике с системами более высокого уровня, такими как SCADA или MES, что способствует цифровой трансформации и созданию умной фабрики в рамках концепции Industry 4.0.   

На рассматриваемом производственном объекте присутствуют четыре ключевых этапа обработки: 
 
## Станция перемещения: 

 ![photo_2024-05-27_18-44-42](https://github.com/Spynch/HS_line316/assets/110130006/954335ad-1ccb-4438-a3f8-2222028dbce3)

1. Два пневматических устройства для выдвижения магазина с компонентами; 
2. Пневматическое устройство захвата; 
3. Два предельных выключателя для фиксации крайних положений захвата; 
4. Сенсоры для определения трех различных положений захвата (центральное, крайнее правое и крайнее левое). 
 
## Станция сверления: 

![photo_2024-05-27_18-44-32](https://github.com/Spynch/HS_line316/assets/110130006/494b93d8-83f6-4c23-a437-ab748e7b1125)

1. Мехатронный блок для проверки расположения заготовки (правильность её ориентации); 
2. Устройство вращающегося стола; 
3. Два индукционных сенсора для определения положения стола; 
4. Два оптических сенсора для распознавания цвета. 
 
## Станция упаковки: 

![photo_2024-05-27_18-44-46](https://github.com/Spynch/HS_line316/assets/110130006/7fd1a6e3-e4ea-4f62-ad4f-d0270033e25f)

1. Сенсоры для определения трех положений захвата (центральное, крайнее правое и крайнее левое); 
2. Модуль для упаковки в картонные коробки; 
3. Четыре цифровых привода для выполнения механических действий по упаковке в картонные коробки; 
4. Четыре дискретных сенсора. 
 
## Станция распределения заготовок: 

 ![photo_2024-05-27_18-44-44](https://github.com/Spynch/HS_line316/assets/110130006/1e70fb35-7167-40b7-9e6b-237a5c021b98)

1. Конвейер с транспортной лентой для перемещения заготовок; 
2. Скаты-накопители для компонентов; 
3. Три устройства для отделения и сортировки заготовок; 
4. Оптические сенсоры для обнаружения наличия изделий на конвейере и скатах.
  
 
## Имитируемый технологический процесс: 
 
### Этап 1 
 
Перемещение захвата на крайнюю левую позицию над магазином фишек (там, где будет выдаваться заготовка). Захват опускается, захватывает фишку и переносит её на станцию сверления. 
 
### Этап 2 
 
Заготовка опускается на поворотный стол. Стол совершает поворотное движение в 4 такта и приходит к модулю проверки положения заготовки. Далее идет оборот стола ещё на один такт, чтобы попасть к модулю сверления. Если заготовка является перевернутой, то модуль сверления опускается. После обработки стол поворачивается к изначальной позиции, обработка детали закончена. 
 
### Этап 3 
 
Захват забирает обработанное изделие и переносит его на станцию упаковки в центральную позицию. Перед этим коробка выходит в позицию готовности и открывается. Затем кладется в коробку и упаковывается. 
 
### Этап 4 
 
Захват переносит коробку в крайнее правое положение и опускает коробку на конвейер. В зависимости от определенного ранее на станции обработки цвета изделия, запускается соответствующий отсекатель и коробка c заготовкой идёт в нужный накопитель. 
 
# Тэги для ПЛК 
 
## Proccesing station PLC
 
processing_input_5_carousel_init - карусель в исходном состоянии 
 
processing_input_6_hole_detected - дырка сверху шайбы 
 
processing_input_1_workpiece_detected - шайба на определении цвета 
 
processing_input_7_workpiece_not_black - датчик для красной и серебристой шайбы 
 
processing_input_2_workpiece_silver - датчик для серебристой шайбы 
 
processing_output_0_drill - включить дрель 
 
processing_output_1_rotate_carousel - включить вращение карусели 
 
processing_output_2_drill_down - опустить дрель 
 
processing_output_3_drill_up - поднять дрель 
 
processing_output_4_fix_workpiece - зафиксировать шайбу 
 
processing_output_5_detect_hole - опустить определитель дырки 
 
## Handling and packing station PLC
 
handling_input_1_gripper_right - гриппер справа 
 
handling_input_2_gripper_start - гриппер над стартом 
 
handling_input_3_gripper_under_packing - гриппер над упаковщиком 
 
## Sorting station PLC 
 
sorting_input_3_box_is_down - коробка упала в желоб со своим цветом 
 
sorting_input_4_box_on_conveyor - коробка на конвейре 
 
sorting_output_0_move_conveyor_right - включить движение конвейера вправо 
 
sorting_output_1_move_conveyor_left - включить движение конвейера влево 
 
sorting_output_2_push_silver_workpiece - толкатель для серебристой шайбы 
 
sorting_output_3_push_red_workpiece - толкатель для красной шайбы

> Кто дочитал до конца - держи креветку :fried_shrimp:
