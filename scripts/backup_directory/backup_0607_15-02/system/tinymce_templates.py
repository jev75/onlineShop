TINYMCE_TEMPLATES = [
    {
        'title': '1. Rėmelis kodui pilkas lightgray',
        'description': 'Kodui lightgray: <div> <pre> <code>',
        'content': '''
        <div style="background-color: lightgray; color: black; border: 1px solid black; margin: 10px; padding: 10px;">
            <pre>
                <code>
def hello_world():
    print("Hello, world!")
                </code>
            </pre>      
        </div>
        <br>        
    ''',
    },
    {
        'title': '2. Rėmelis kodui melsvas lightcyan',
        'description': ' lightcyan: <div> <pre> <code>',
        'content': '''
        <div style="background-color: lightcyan; color: black; border: 1px solid black; margin: 10px; padding: 10px;">
            
                <code>
def hello_world():
    print("Hello, world!")
                </code>
                 
        </div>
        <br>        
    ''',
    },
    {
        'title': '2.1. Rėmelis kodui Žalsvas WhiteSmoke ',
        'description': ' fonas Žalsvas WhiteSmoke',
        'content': '''
        <div style="background-color: WhiteSmoke; color: black; border: 1px solid black; margin: 10px; padding: 10px;">
<pre id="python-code">
                <code>
def hello_world():    
                </code>
</pre>

        </div>
        <br>        
    ''',
    },
    {
        'title': '3. fonas rėmelyje lengvai melsvas LightCyan',
        'description': 'fonas rėmelyje lengvai melsvas LightCyan',
        'content': '''
         <div style="background: rgba(224, 255, 255, 0.5); color: black; border: 1px solid black; margin: 10px; padding: 10px;">
            <h2>Python</h2>
            <p>Kažką apie Python.</p>
        </div>
        <br>   
    ''',
    },
    {
        'title': '4. fonas lengvai žalias YellowGreen',
        'description': 'fonas lengvai žalias YellowGreen',
        'content': '''
<div style="background: rgba(154, 205, 50, 0.1); color: black; margin: 10px; padding: 10px;">
            <h2>Python</h2>
            <p>Kažką apie Python.</p>
        </div>
        <br>   
    ''',
    },
    {
        'title': '5. fonas rėmelyje WhiteSmoke',
        'description': 'fonas Žalsvas WhiteSmoke',
        'content': '''
        <div style="background: rgba(245, 245, 245); color: black; border: 1px solid black; margin: 10px; padding: 10px;">
            <h2>Python</h2>
            <p>Kažką apie Python.</p>
        </div>
        <br>    
    ''',
    },

    {
        'title': '6. Copy to.. Versija 1',
        'description': 'Copy to.. Versija 1',
        'content': '''
        <script src="https://cdn.jsdelivr.net/clipboard.js/1.6.1/clipboard.min.js"></script>
    <pre><code id="python">
def saraso_skaiciu_suma(sarasas):
    viso = 0
    for skaicius in sarasas:
        viso += skaicius
    return viso     
</code></pre>
</div>
<button data-clipboard-target="#python" class="button">Copy</button>
<script>
        var clipboard = new Clipboard('button');
</script>
        ''',
    },
    {
        'title': '7. Copy to.. Versija 2',
        'description': 'Copy to.. Versija 2',
        'content': '''
            <script src="https://cdn.jsdelivr.net/clipboard.js/1.6.1/clipboard.min.js"></script>
    <pre><code id="pythonC">
def saraso_skaiciu_suma(sarasas):
    viso = 0
    for skaicius in sarasas:
        viso += skaicius
    return viso     
</code></pre>
</div>
<button data-clipboard-target="#pythonC" class="button">Copy</button>
<script>
        var clipboard = new Clipboard('button');
</script>
        ''',
    },

{
    'title': '8. Copy to.. Versija 3',
    'description': 'Copy to.. Versija 3',
    'content': '''    
    <script src="https://cdn.jsdelivr.net/clipboard.js/1.6.1/clipboard.min.js"></script>
    <pre><code id="pythonCode">
def saraso_skaiciu_suma(sarasas):
    viso = 0
    for skaicius in sarasas:
        viso += skaicius
    return viso     
</code></pre>
</div>
<button data-clipboard-target="#pythonCode" class="button">Copy</button>
<script>
        var clipboard = new Clipboard('button');
</script>
'''
},
{
    'title': '9. Copy to.. Versija 4',
    'description': 'Copy to.. Versija 4',
    'content': '''    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.8/clipboard.min.js"></script>
    <style>       
        pre#python-code {
            background-color: #f0f0f0; 
            padding: 10px;
            border: 1px solid #ccc; 
            border-radius: 5px;
            overflow-x: auto; 
        }
    </style>
   <pre id="python-code">
        <code>
def hello_world():
    print("Hello, world!")
        </code>
    </pre>
    <button id="copy-button" data-clipboard-target="#python-code">
    Copy
</button>
<script>
        var clipboard = new ClipboardJS('#copy-button');
</script>
'''
},
{
    'title': '10. Copy to.. Versija 5',
    'description': 'Copy to.. Versija 5',
    'content': '''    
       <script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.8/clipboard.min.js"></script>
       <style>       
        pre#pythonB {
            background-color: LightCyan; 
            padding: 10px;
            border: 1px solid #ccc; 
            border-radius: 5px;
            overflow-x: auto; 
        }
    </style>
  <pre id="pythonB">
        <code>
def hello_world():
    print("Hello, world!")
        </code>
    </pre>
         <button id="copy-button" data-clipboard-target="#pythonB">
 Copy 
</button>
'''
},
    {
        'title': '11. Logotipas',
        'description': 'Paveikslėlis su tekstu',
        'content': '''
        <style>
    .logo-image {
        position: relative;
        display: inline-block;
        max-width: 100%;
    }

    .logo-image image {
        display: block;
        max-width: 100%;
        opacity: 0.7; /* Pusiau peršviečiamas */
    }

    .logo-image .logo-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        font-size: 24px;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
</style>
<div class="logo-image">
    <image src="path_to_your_image.jpg" alt="Logo">
    <div class="logo-text">Jūsų Tekstas Čia</div>
</div>

     ''',
    },
  {
        'title': '12. Spalva Kodui WhiteSmoke',
        'description': 'Spalva Kodui',
        'content': '''
        <div style="background-color: WhiteSmoke; color: black; border: 1px solid black; margin: 10px; padding: 10px;">
    <pre><code class="language-python">
def hello_world():
    print("Hello, world!")
    </code></pre>  
        </div>
        <br>
     ''',
    },
{
        'title': '13. Spalva Kintamieisiems WhiteSmoke',
        'description': 'Spalva Kodui',
        'content': '''
        <div style="background-color: WhiteSmoke; color: black; border: 1px solid black; margin: 10px; padding: 10px;">
    <pre><code class="language-python">
x = 5
vardas = "Jonas"
amzius = 25
</code></pre>
        </div>
        <br>
     ''',
    },

]
