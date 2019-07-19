import os


def vtt_to_srt():
    main_dir = os.getcwd()
    all_folders = os.listdir()

    for folder in all_folders:
        os.chdir(main_dir)
        if os.path.isdir(folder):
            os.chdir(folder)
            files_list = os.listdir(os.getcwd())
            for instance in files_list:
                if instance.endswith('.vtt'):
                    curr_dir = os.getcwd()
                    name_extenstion = os.path.splitext(instance)
                    
                    old = curr_dir + '/' + instance
                    new = curr_dir + '/' + name_extenstion[0] + '.srt'
                    print()
                    print()
                    print(old)
                    print(new)
                    print()
                    print()
                    os.system(
                        "ffmpeg -i  '{source}' '{destination}'".format(
                            source=old,
                            destination=new)
                    )


vtt_to_srt()
