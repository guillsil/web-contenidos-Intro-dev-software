from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

#Decorador 
@app.route("/")
def index():
    return render_template("index.html")

dic_comados = {
    "awk": "Lenguaje de búsqueda y procesamiento de patrones.",
    "cat": "Muestra el contenido de uno o varios archivos.",
    "cut": "Extrae campos seleccionados de cada línea de un archivo.",
    "diff": "Compara dos archivos línea por línea.",
    "grep": "Busca patrones en un archivo.",
    "head": "Muestra las primeras líneas de un archivo.",
    "less": "Permite visualizar un archivo de texto.",
    "sed": "Editor de secuencias (especialmente para buscar y reemplazar).",
    "sort": "Ordena las líneas de un archivo.",
    "split": "Divide un archivo en partes más pequeñas.",
    "tr": "Traduce o elimina caracteres.",
    "uniq": "Encuentra líneas duplicadas en un archivo.",
    "wc": "Cuenta líneas, palabras y caracteres en un archivo.",
    "touch": "Crea un archivo vacío.",
}
@app.route("/procesamiento-de-archivos-en-bash")
def page_procesamiento_de_archivos():
    return render_template("procesamiento.html", dic_comados=dic_comados)

@app.route("/que-es-un-script")
def page_que_es_un_script():
    return render_template("que-es-un-script.html")

@app.route("/variables-globales-y-locales")
def page_variables_globales_y_locales():
    return render_template("variables-locales-globales.html")

@app.route("/estructuras-de-control-e-iteracion-en-bash")
def page_estructuras_de_control_e_iterativas():
    return render_template("estructuras-de-control-e-iterativas.html")

@app.route("/ejercicios-de-bash")
def page_ejercicios_en_bash():
    return render_template("ejercicios-bash.html")

@app.route("/comandos-comunmente-utilizados")
def page_comandos_comunmente_utilizados():
    return render_template("comandos_usados.html")

@app.route("/comparar-condicionales-bash")
def page_comparar_condicionales_bash():
    return render_template("comparar-Condicionales.html")

@app.route("/diferencias-entre-while-y-until")
def page_diferencias_entre_while_y_until():
    return render_template("diferencia-entre-while-until.html")

@app.route("/estructura-del-case-en-bash")
def page_estructura_del_case_en_bash():
    return render_template("estructura-case.html")

@app.route("/introduccion-a-las-exprexiones-regulares")
def page_introduccion_a_las_expresiones_regulares():
    return render_template("expresiones-regulares.html")

@app.route("/sed-y-grep")
def page_sed_y_grep():
    return render_template("que-es-Sed-Grep.html")

@app.route("/pipeline")
def page_pipeline():
    return render_template("que-es-un-Pipeline.html")

@app.route("/operadores-de-redireccion-en-bash")
def page_operadores_de_redireccion_en_bash():
    return render_template("que-son-los-Operadores-de-Redireccion.html")

@app.route("/entornos-virtuales")
def page_entornos_virtuales():
    return render_template("entorno-Virtuales.html")

@app.route("/introduccion-a-flask")
def page_introduccion_a_flask():
    return render_template("flask.html")

@app.route("/introduccion-al-desarrollo-web")
def page_introduccion_al_desarrollo_web():
    return render_template("introduccion-Desarrollode-Web.html")

@app.route("/scripts-para-preparar-flask")
def page_scripts_para_flask():
    return render_template("scripts-para-preparar-flask.html")

@app.route("/flask")
def page_flask():
    return render_template("flask-two.html")

@app.route("/introduccion-a-html")
def page_introduccion_a_html():
    return render_template("html.html")

@app.route("/introduccion-a-css")
def page_introduccion_a_css():
    return render_template("css.html")

@app.route("/introduccion-a-javascript")
def page_introduccion_a_javascript():
    return render_template("javascript.html")

@app.route("/blocks-en-flask")
def page_blocks_en_flask():
    return render_template("blocks.html")

@app.route("/errorHandlers-en-flask")
def page_errorHandlers_en_flask():
    return render_template("errorHandlers.html")

@app.route("/formularios-en-flask")
def page_formularios_en_flask():
    return render_template("formularios-flask.html")

@app.route("/como-poner-y-modificar-links-en-flask")
def page_como_poner_y_modificar_links_en_flask():
    return render_template("modificacion-urls-links.html")

@app.route("/como-usar-ciclos-en-flask")
def page_como_usar_ciclos_en_flask():
    return render_template("uso-de-ciclos-flask.html")


@app.route("/como-hacer-test-en-python")
def page_como_hacer_test_en_python():
    return render_template("como-hacer-test-en-python.html")

@app.route("/introduccion-a-tdd")
def page_introduccion_a_tdd():
    return render_template("tdd.html")


@app.route("/como-usar-gdb")
def page_como_usar_gdb():
    return render_template("gdb.html")


@app.route("/bugs")
def page_bugs():
    return render_template("que-es-un-bugs-tipos.html")

@app.route("/como-implementar-kanban")
def page_como_implementar_kanban():
    return render_template("kanban.html")

@app.route("/introduccion-a-scrum")
def page_introduccion_a_scrum():
    return render_template("scrum.html")

@app.route("/proyectos")
def page_proyectos():
    return render_template("proyectos.html")

@app.route("/repaso-parcial")
def page_repaso_para_el_parcial():
    return render_template("repaso-parcial.html")

@app.route("/parcial")
def page_parcial():
    return render_template("parcial.html")

@app.route("/parcial-resolucion")
def page_parcial_resuelto():
    return render_template("parcial-resuelto.html")

@app.route("/feddback")
def page_feedback():
    return render_template("feedback.html")

@app.route("/soy")
def page_soy():
    return render_template("soy.html")

@app.route("/contacto")
def page_contacto():
    return render_template("contacto.html")


@app.route("/form_feedback", methods=['GET', 'POST'])
def form_feedback():
    if request.method == 'POST':
        name = request.form.get('name', '')
        lastname = request.form.get('lastname', '')
        mail = request.form.get('email', '')
        message = request.form.get('feedback', '')
        if name and lastname and mail and message: 
            return render_template('gracias.html', name=name, lastname=lastname)
        else:
            return render_template('404.html')
    return render_template('404.html')

@app.route("/api")
def page_api():
    return render_template("api.html")



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run("127.0.0.1", port=5001, debug=True)
    
