# MAXINE-VFX-SDK_video_stream
Данный репозиторий можно использовать для увеличения качества видео и его разрешения на основе нейронных сетей от Nvidia.

Выполнено на основе:
[MAXINE-VFX-SDK](https://github.com/NVIDIA/MAXINE-VFX-SDK.git)

Код в репозитории работает с помощью команд интерфейса CLI.

Доступны следующие преобразования видео:
- **Upscale** - увеличивает разрешение входного видео. Во время работы применяются по умолчанию также алгоритмы:
  - **Artifact Reduction** - эффект исключения искажений;
  - **Super Resolution** - эффект улучшения деталей и четкости;
- **Denoising** - эффект удаления шума.

Каждый эффект можно также применять отдельно ко всему видео. Это позволяет выстраивать цепочки последовательных преобразований в желаемом порядке.

Чтобы применить каждый эффект в желаемом порядке за одно преобразование (в потоке) необходимо декодировать видео, выполнить необходимые преобразования каждого кадра, а затем энкодером преобразовывать их в выходное видео.

Одновременно Artifact Reduction и Super Resolution доступны по умолчанию только с Upscale.

# Требования к системе
Библиотека работает на компьютерах с видеокартами, имеющими архитектуру Turing или Ampere от NVIDIA.

Поддерживается 64-разрядная версия Windows 10 или более поздняя.

Графический драйвер NVIDIA для Windows должен быть 465.89 или более поздней версии.

# Использование
1. Установить [SDK](https://www.nvidia.com/ru-ru/geforce/broadcasting/broadcast-sdk/resources/):
    - [Ссылка](https://international.download.nvidia.com/Windows/broadcast/sdk/v0.6.5/nvidia_video_effects_sdk_installer_ampere.exe) для видеокарт NVIDIA GeForce RTX 30 или профессиональных графических процессоров NVIDIA RTX.
    - [Ссылка](https://international.download.nvidia.com/Windows/broadcast/sdk/v0.6.5/nvidia_video_effects_sdk_installer_turing.exe) для видеокарт NVIDIA GeForce RTX 20 или NVIDIA Quadro RTX.
2. Установить Python >= 3.8.
3. В командной строке Windows:
    - Скачать текущий репозиторий: git clone https://github.com/uralskayamariya/MAXINE-VFX-SDK_video_stream.git
    - Перейти в папку текущего репозитория: cd MAXINE-VFX-SDK_video_stream
    - Запустить скрипт run.py: python run.py
    - Ввести данные, которые запрашивает программа:
      * Выбрать алгоритм:
         - 1-Upscale (включает Artifact Reduction, Super Resolution) (Допускается масштаб от размера входного изображения по вертикали 1.3333x, 1.5x, 2x, 3x или 4x.)
         - 2-Denoising
         - 3-Artifact Reduction
         - 4-Super Resolution (Допускается масштаб от размера входного изображения по вертикали 1.3333x, 1.5x, 2x, 3x или 4x.)
      * Указать путь ко входному видео. Если положить видео в папку input в текущем каталоге, можно указать только его имя, например: input_video.mp4
      * Указать путь к выходному видео. Если хотите сохранить видео в папку output в текущем каталоге, можно указать только его имя, например: output_video.mp4. Папка output должна быть создана заранее.

# Документация
* [NVIDIA Video Effects SDK Programming Guide](https://docs.nvidia.com/deeplearning/maxine/vfx-sdk-programming-guide/index.html)
* [NVIDIA Video Effects SDK System Guide](https://docs.nvidia.com/deeplearning/maxine/vfx-sdk-system-guide/index.html)
* [NvCVImage API Guide](https://docs.nvidia.com/deeplearning/maxine/nvcvimage-api-guide/index.html)

PDF версии доступны по следующим ссылкам: 
* [NVIDIA Video Effects SDK Programming Guide](https://docs.nvidia.com/deeplearning/maxine/pdf/vfx-sdk-programming-guide.pdf)
* [NVIDIA Video Effects SDK System Guide](https://docs.nvidia.com/deeplearning/maxine/pdf/vfx-sdk-system-guide.pdf)
* [NvCVImage API Guide](https://docs.nvidia.com/deeplearning/maxine/pdf/nvcvimage-api-guide.pdf)
