import os
import subprocess
import shlex


def main():
    working_directory = os.getcwd()

    effect = int(input('Выберите эффект, указав его номер: 1-Upscale, 2-Denoising, 3-Artifact Reduction, 4-Super Resolution: '))
    inp_path = str(input('Введите путь ко входному видео: '))
    out_path = str(input('Введите путь к выходному видео: '))

    if len(inp_path.split('/')) == 1:
        inp_path = f'input/{inp_path}'
    if len(out_path.split('/')) == 1:
        out_path = f'output/{out_path}'

    if effect == 1:
        res = float(input('Введите разрешение по вертикали для выходного видео (Допускается масштаб от размера входного изображения 1.3333x, 1.5x, 2x, 3x или 4x): '))
        cmd = "UpscalePipelineApp.exe --in_file='{}' --upscale_strength=1 --resolution={} --ar_mode=1 --show --out_file='{}' --verbose".format(inp_path, res, out_path)
        p = subprocess.Popen(shlex.split(cmd), cwd=working_directory)
        p.wait()
    elif effect == 2:
        cmd = "DenoiseEffectApp.exe --in_file='{}' --strength=1 --show --out_file='{}' --verbose".format(inp_path, out_path)
        p = subprocess.Popen(shlex.split(cmd), cwd=working_directory)
        p.wait()
    else:
        if effect == 3:
            cmd = "VideoEffectsApp.exe --in_file='{}' --effect=ArtifactReduction --mode=1 --show --out_file='{}' --verbose".format(inp_path, out_path)
            p = subprocess.Popen(shlex.split(cmd), cwd=working_directory)
            p.wait()
        else:
            res = float(input('Введите разрешение по вертикали для выходного видео (Допускается масштаб от размера входного изображения 1.3333x, 1.5x, 2x, 3x или 4x): '))
            cmd = "VideoEffectsApp.exe --in_file='{}' --effect=SuperRes --mode=1 --resolution={} --show --out_file='{}' --verbose".format(inp_path, res, out_path)
            p = subprocess.Popen(shlex.split(cmd), cwd=working_directory)
            p.wait()

if __name__ == '__main__':
    main() 