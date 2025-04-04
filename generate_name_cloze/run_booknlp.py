from booknlp.booknlp import BookNLP
import sys, re

model_params={
        # for name cloze, we just need the entity tagger
        "pipeline":"entity", 

        # but if you want to run all of booknlp over the book anyway, use this instead
        # "pipeline":"entity,quote,supersense,event,coref",

        "model":"big"
    }
    
booknlp=BookNLP("en", model_params)

input_file= "A_tramp_abroad.txt"
output_id= "A_tramp_abroad"

with open(input_file) as file:

        output_directory="booknlp_output/%s" % output_id
        booknlp.process(input_file, output_directory, output_id)
