# server.py
# Math tools web application
# Author: Sébastien Combéfis
# Version: February 8, 2018

import cherrypy
import utils
import re

class WebApp():
    @cherrypy.expose
    def index(self):
        return 
            '''
            <h2>Coucou</h2>
            <form method="post" action="computeFactoriel" title="Factoriel">
                <p>
                    <label>Entrez un nombre positif : </label> <input type="number" name="inputNumber"/>
                </p>
                <p>
                    <label>Réponse :</label>
                    {{content}}
                </p>
            </form>
            '''
    
    def computeFactoriel (self, inputNumber):
        pattern = "^\d+$"
        p = re.compile (pattern)
        if p.match (inputNumber) is not None :
            content = str (utils.fact (int (inputNumber))
        else :
            content = "Veuillez entrer un nombre positif"
        return {'content': content}

cherrypy.quickstart(WebApp(), '', 'server.conf')
