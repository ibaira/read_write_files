FROM python:3.5

ADD scripts/read_write_files.py /

ADD scripts/input_files /input_files

ADD scripts/output_files /output_files 

CMD [ "python3", "read_write_files.py" ]

