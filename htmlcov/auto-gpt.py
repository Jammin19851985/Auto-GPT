print()
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Coverage for autogpt/prompts/generator.py: 89%</title>
    <link rel="icon" sizes="32x32" href="favicon_32.png">
    <link rel="stylesheet" href="style.css" type="text/css">
    <script type="text/javascript" src="coverage_html.js" defer></script>
</head>
<body class="pyfile">
<header>
    <div class="content">
        <h1>
            <span class="text">Coverage for </span><b>autogpt/prompts/generator.py</b>:
            <span class="pc_cov">89%</span>
        </h1>
        <aside id="help_panel_wrapper">
            <input id="help_panel_state" type="checkbox">
            <label for="help_panel_state">
                <img id="keyboard_icon" src="keybd_closed.png" alt="Show/hide keyboard shortcuts" />
            </label>
            <div id="help_panel">
                <p class="legend">Shortcuts on this page</p>
                <div class="keyhelp">
                    <p>
                        <kbd>r</kbd>
                        <kbd>m</kbd>
                        <kbd>x</kbd>
                        <kbd>p</kbd>
                        &nbsp; toggle line displays
                    </p>
                    <p>
                        <kbd>j</kbd>
                        <kbd>k</kbd>
                        &nbsp; next/prev highlighted chunk
                    </p>
                    <p>
                        <kbd>0</kbd> &nbsp; (zero) top of page
                    </p>
                    <p>
                        <kbd>1</kbd> &nbsp; (one) first highlighted chunk
                    </p>
                    <p>
                        <kbd>[</kbd>
                        <kbd>]</kbd>
                        &nbsp; prev/next file
                    </p>
                    <p>
                        <kbd>u</kbd> &nbsp; up to the index
                    </p>
                    <p>
                        <kbd>?</kbd> &nbsp; show/hide this help
                    </p>
                </div>
            </div>
        </aside>
        <h2>
            <span class="text">39 statements &nbsp;</span>
            <button type="button" class="run button_toggle_run" value="run" data-shortcut="r" title="Toggle lines run">37<span class="text"> run</span></button>
            <button type="button" class="mis show_mis button_toggle_mis" value="mis" data-shortcut="m" title="Toggle lines missing">2<span class="text"> missing</span></button>
            <button type="button" class="exc show_exc button_toggle_exc" value="exc" data-shortcut="x" title="Toggle lines excluded">0<span class="text"> excluded</span></button>
            <button type="button" class="par run show_par button_toggle_par" value="par" data-shortcut="p" title="Toggle lines partially run">2<span class="text"> partial</span></button>
        </h2>
        <p class="text">
            <a id="prevFileLink" class="nav" href="d_ed286290bb007969_text_py.html">&#xab; prev</a> &nbsp; &nbsp;
            <a id="indexLink" class="nav" href="index.html">&Hat; index</a> &nbsp; &nbsp;
            <a id="nextFileLink" class="nav" href="d_e1c04ba85fbf6b91_prompt_py.html">&#xbb; next</a>
            &nbsp; &nbsp; &nbsp;
            <a class="nav" href="https://coverage.readthedocs.io/en/7.2.3">coverage.py v7.2.3</a>,
            created at 2023-04-22 05:45 +0000
        </p>
        <aside class="hidden">
            <button type="button" class="button_next_chunk" data-shortcut="j"/>
            <button type="button" class="button_prev_chunk" data-shortcut="k"/>
            <button type="button" class="button_top_of_page" data-shortcut="0"/>
            <button type="button" class="button_first_chunk" data-shortcut="1"/>
            <button type="button" class="button_prev_file" data-shortcut="["/>
            <button type="button" class="button_next_file" data-shortcut="]"/>
            <button type="button" class="button_to_index" data-shortcut="u"/>
            <button type="button" class="button_show_hide_help" data-shortcut="?"/>
        </aside>
    </div>
</header>
<main id="source">
    <p class="pln"><span class="n"><a id="t1" href="#t1">1</a></span><span class="t"><span class="str">""" A module for generating custom prompt strings."""</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t2" href="#t2">2</a></span><span class="t"><span class="key">import</span> <span class="nam">json</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t3" href="#t3">3</a></span><span class="t"><span class="key">from</span> <span class="nam">typing</span> <span class="key">import</span> <span class="nam">Any</span><span class="op">,</span> <span class="nam">Callable</span><span class="op">,</span> <span class="nam">Dict</span><span class="op">,</span> <span class="nam">List</span><span class="op">,</span> <span class="nam">Optional</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t4" href="#t4">4</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t5" href="#t5">5</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t6" href="#t6">6</a></span><span class="t"><span class="key">class</span> <span class="nam">PromptGenerator</span><span class="op">:</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t7" href="#t7">7</a></span><span class="t">    <span class="str">"""</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t8" href="#t8">8</a></span><span class="t"><span class="str">    A class for generating custom prompt strings based on constraints, commands,</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t9" href="#t9">9</a></span><span class="t"><span class="str">        resources, and performance evaluations.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t10" href="#t10">10</a></span><span class="t"><span class="str">    """</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t11" href="#t11">11</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t12" href="#t12">12</a></span><span class="t">    <span class="key">def</span> <span class="nam">__init__</span><span class="op">(</span><span class="nam">self</span><span class="op">)</span> <span class="op">-></span> <span class="key">None</span><span class="op">:</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t13" href="#t13">13</a></span><span class="t">        <span class="str">"""</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t14" href="#t14">14</a></span><span class="t"><span class="str">        Initialize the PromptGenerator object with empty lists of constraints,</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t15" href="#t15">15</a></span><span class="t"><span class="str">            commands, resources, and performance evaluations.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t16" href="#t16">16</a></span><span class="t"><span class="str">        """</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t17" href="#t17">17</a></span><span class="t">        <span class="nam">self</span><span class="op">.</span><span class="nam">constraints</span> <span class="op">=</span> <span class="op">[</span><span class="op">]</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t18" href="#t18">18</a></span><span class="t">        <span class="nam">self</span><span class="op">.</span><span class="nam">commands</span> <span class="op">=</span> <span class="op">[</span><span class="op">]</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t19" href="#t19">19</a></span><span class="t">        <span class="nam">self</span><span class="op">.</span><span class="nam">resources</span> <span class="op">=</span> <span class="op">[</span><span class="op">]</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t20" href="#t20">20</a></span><span class="t">        <span class="nam">self</span><span class="op">.</span><span class="nam">performance_evaluation</span> <span class="op">=</span> <span class="op">[</span><span class="op">]</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t21" href="#t21">21</a></span><span class="t">        <span class="nam">self</span><span class="op">.</span><span class="nam">goals</span> <span class="op">=</span> <span class="op">[</span><span class="op">]</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t22" href="#t22">22</a></span><span class="t">        <span class="nam">self</span><span class="op">.</span><span class="nam">command_registry</span> <span class="op">=</span> <span class="key">None</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t23" href="#t23">23</a></span><span class="t">        <span class="nam">self</span><span class="op">.</span><span class="nam">name</span> <span class="op">=</span> <span class="str">"Bob"</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t24" href="#t24">24</a></span><span class="t">        <span class="nam">self</span><span class="op">.</span><span class="nam">role</span> <span class="op">=</span> <span class="str">"AI"</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t25" href="#t25">25</a></span><span class="t">        <span class="nam">self</span><span class="op">.</span><span class="nam">response_format</span> <span class="op">=</span> <span class="op">{</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t26" href="#t26">26</a></span><span class="t">            <span class="str">"thoughts"</span><span class="op">:</span> <span class="op">{</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t27" href="#t27">27</a></span><span class="t">                <span class="str">"text"</span><span class="op">:</span> <span class="str">"thought"</span><span class="op">,</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t28" href="#t28">28</a></span><span class="t">                <span class="str">"reasoning"</span><span class="op">:</span> <span class="str">"reasoning"</span><span class="op">,</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t29" href="#t29">29</a></span><span class="t">                <span class="str">"plan"</span><span class="op">:</span> <span class="str">"- short bulleted\n- list that conveys\n- long-term plan"</span><span class="op">,</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t30" href="#t30">30</a></span><span class="t">                <span class="str">"criticism"</span><span class="op">:</span> <span class="str">"constructive self-criticism"</span><span class="op">,</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t31" href="#t31">31</a></span><span class="t">                <span class="str">"speak"</span><span class="op">:</span> <span class="str">"thoughts summary to say to user"</span><span class="op">,</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t32" href="#t32">32</a></span><span class="t">            <span class="op">}</span><span class="op">,</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t33" href="#t33">33</a></span><span class="t">            <span class="str">"command"</span><span class="op">:</span> <span class="op">{</span><span class="str">"name"</span><span class="op">:</span> <span class="str">"command name"</span><span class="op">,</span> <span class="str">"args"</span><span class="op">:</span> <span class="op">{</span><span class="str">"arg name"</span><span class="op">:</span> <span class="str">"value"</span><span class="op">}</span><span class="op">}</span><span class="op">,</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t34" href="#t34">34</a></span><span class="t">        <span class="op">}</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t35" href="#t35">35</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t36" href="#t36">36</a></span><span class="t">    <span class="key">def</span> <span class="nam">add_constraint</span><span class="op">(</span><span class="nam">self</span><span class="op">,</span> <span class="nam">constraint</span><span class="op">:</span> <span class="nam">str</span><span class="op">)</span> <span class="op">-></span> <span class="key">None</span><span class="op">:</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t37" href="#t37">37</a></span><span class="t">        <span class="str">"""</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t38" href="#t38">38</a></span><span class="t"><span class="str">        Add a constraint to the constraints list.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t39" href="#t39">39</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t40" href="#t40">40</a></span><span class="t"><span class="str">        Args:</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t41" href="#t41">41</a></span><span class="t"><span class="str">            constraint (str): The constraint to be added.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t42" href="#t42">42</a></span><span class="t"><span class="str">        """</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t43" href="#t43">43</a></span><span class="t">        <span class="nam">self</span><span class="op">.</span><span class="nam">constraints</span><span class="op">.</span><span class="nam">append</span><span class="op">(</span><span class="nam">constraint</span><span class="op">)</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t44" href="#t44">44</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t45" href="#t45">45</a></span><span class="t">    <span class="key">def</span> <span class="nam">add_command</span><span class="op">(</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t46" href="#t46">46</a></span><span class="t">        <span class="nam">self</span><span class="op">,</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t47" href="#t47">47</a></span><span class="t">        <span class="nam">command_label</span><span class="op">:</span> <span class="nam">str</span><span class="op">,</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t48" href="#t48">48</a></span><span class="t">        <span class="nam">command_name</span><span class="op">:</span> <span class="nam">str</span><span class="op">,</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t49" href="#t49">49</a></span><span class="t">        <span class="nam">args</span><span class="op">=</span><span class="key">None</span><span class="op">,</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t50" href="#t50">50</a></span><span class="t">        <span class="nam">function</span><span class="op">:</span> <span class="nam">Optional</span><span class="op">[</span><span class="nam">Callable</span><span class="op">]</span> <span class="op">=</span> <span class="key">None</span><span class="op">,</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t51" href="#t51">51</a></span><span class="t">    <span class="op">)</span> <span class="op">-></span> <span class="key">None</span><span class="op">:</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t52" href="#t52">52</a></span><span class="t">        <span class="str">"""</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t53" href="#t53">53</a></span><span class="t"><span class="str">        Add a command to the commands list with a label, name, and optional arguments.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t54" href="#t54">54</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t55" href="#t55">55</a></span><span class="t"><span class="str">        Args:</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t56" href="#t56">56</a></span><span class="t"><span class="str">            command_label (str): The label of the command.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t57" href="#t57">57</a></span><span class="t"><span class="str">            command_name (str): The name of the command.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t58" href="#t58">58</a></span><span class="t"><span class="str">            args (dict, optional): A dictionary containing argument names and their</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t59" href="#t59">59</a></span><span class="t"><span class="str">              values. Defaults to None.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t60" href="#t60">60</a></span><span class="t"><span class="str">            function (callable, optional): A callable function to be called when</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t61" href="#t61">61</a></span><span class="t"><span class="str">                the command is executed. Defaults to None.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t62" href="#t62">62</a></span><span class="t"><span class="str">        """</span>&nbsp;</span><span class="r"></span></p>
    <p class="par run show_par"><span class="n"><a id="t63" href="#t63">63</a></span><span class="t">        <span class="key">if</span> <span class="nam">args</span> <span class="key">is</span> <span class="key">None</span><span class="op">:</span>&nbsp;</span><span class="r"><span class="annotate short">63&#x202F;&#x219B;&#x202F;64</span><span class="annotate long">line 63 didn't jump to line 64, because the condition on line 63 was never true</span></span></p>
    <p class="mis show_mis"><span class="n"><a id="t64" href="#t64">64</a></span><span class="t">            <span class="nam">args</span> <span class="op">=</span> <span class="op">{</span><span class="op">}</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t65" href="#t65">65</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t66" href="#t66">66</a></span><span class="t">        <span class="nam">command_args</span> <span class="op">=</span> <span class="op">{</span><span class="nam">arg_key</span><span class="op">:</span> <span class="nam">arg_value</span> <span class="key">for</span> <span class="nam">arg_key</span><span class="op">,</span> <span class="nam">arg_value</span> <span class="key">in</span> <span class="nam">args</span><span class="op">.</span><span class="nam">items</span><span class="op">(</span><span class="op">)</span><span class="op">}</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t67" href="#t67">67</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t68" href="#t68">68</a></span><span class="t">        <span class="nam">command</span> <span class="op">=</span> <span class="op">{</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t69" href="#t69">69</a></span><span class="t">            <span class="str">"label"</span><span class="op">:</span> <span class="nam">command_label</span><span class="op">,</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t70" href="#t70">70</a></span><span class="t">            <span class="str">"name"</span><span class="op">:</span> <span class="nam">command_name</span><span class="op">,</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t71" href="#t71">71</a></span><span class="t">            <span class="str">"args"</span><span class="op">:</span> <span class="nam">command_args</span><span class="op">,</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t72" href="#t72">72</a></span><span class="t">            <span class="str">"function"</span><span class="op">:</span> <span class="nam">function</span><span class="op">,</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t73" href="#t73">73</a></span><span class="t">        <span class="op">}</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t74" href="#t74">74</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t75" href="#t75">75</a></span><span class="t">        <span class="nam">self</span><span class="op">.</span><span class="nam">commands</span><span class="op">.</span><span class="nam">append</span><span class="op">(</span><span class="nam">command</span><span class="op">)</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t76" href="#t76">76</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t77" href="#t77">77</a></span><span class="t">    <span class="key">def</span> <span class="nam">_generate_command_string</span><span class="op">(</span><span class="nam">self</span><span class="op">,</span> <span class="nam">command</span><span class="op">:</span> <span class="nam">Dict</span><span class="op">[</span><span class="nam">str</span><span class="op">,</span> <span class="nam">Any</span><span class="op">]</span><span class="op">)</span> <span class="op">-></span> <span class="nam">str</span><span class="op">:</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t78" href="#t78">78</a></span><span class="t">        <span class="str">"""</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t79" href="#t79">79</a></span><span class="t"><span class="str">        Generate a formatted string representation of a command.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t80" href="#t80">80</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t81" href="#t81">81</a></span><span class="t"><span class="str">        Args:</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t82" href="#t82">82</a></span><span class="t"><span class="str">            command (dict): A dictionary containing command information.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t83" href="#t83">83</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t84" href="#t84">84</a></span><span class="t"><span class="str">        Returns:</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t85" href="#t85">85</a></span><span class="t"><span class="str">            str: The formatted command string.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t86" href="#t86">86</a></span><span class="t"><span class="str">        """</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t87" href="#t87">87</a></span><span class="t">        <span class="nam">args_string</span> <span class="op">=</span> <span class="str">", "</span><span class="op">.</span><span class="nam">join</span><span class="op">(</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t88" href="#t88">88</a></span><span class="t">            <span class="str">f'"{key}": "{value}"'</span> <span class="key">for</span> <span class="nam">key</span><span class="op">,</span> <span class="nam">value</span> <span class="key">in</span> <span class="nam">command</span><span class="op">[</span><span class="str">"args"</span><span class="op">]</span><span class="op">.</span><span class="nam">items</span><span class="op">(</span><span class="op">)</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t89" href="#t89">89</a></span><span class="t">        <span class="op">)</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t90" href="#t90">90</a></span><span class="t">        <span class="key">return</span> <span class="str">f'{command["label"]}: "{command["name"]}", args: {args_string}'</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t91" href="#t91">91</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t92" href="#t92">92</a></span><span class="t">    <span class="key">def</span> <span class="nam">add_resource</span><span class="op">(</span><span class="nam">self</span><span class="op">,</span> <span class="nam">resource</span><span class="op">:</span> <span class="nam">str</span><span class="op">)</span> <span class="op">-></span> <span class="key">None</span><span class="op">:</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t93" href="#t93">93</a></span><span class="t">        <span class="str">"""</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t94" href="#t94">94</a></span><span class="t"><span class="str">        Add a resource to the resources list.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t95" href="#t95">95</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t96" href="#t96">96</a></span><span class="t"><span class="str">        Args:</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t97" href="#t97">97</a></span><span class="t"><span class="str">            resource (str): The resource to be added.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t98" href="#t98">98</a></span><span class="t"><span class="str">        """</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t99" href="#t99">99</a></span><span class="t">        <span class="nam">self</span><span class="op">.</span><span class="nam">resources</span><span class="op">.</span><span class="nam">append</span><span class="op">(</span><span class="nam">resource</span><span class="op">)</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t100" href="#t100">100</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t101" href="#t101">101</a></span><span class="t">    <span class="key">def</span> <span class="nam">add_performance_evaluation</span><span class="op">(</span><span class="nam">self</span><span class="op">,</span> <span class="nam">evaluation</span><span class="op">:</span> <span class="nam">str</span><span class="op">)</span> <span class="op">-></span> <span class="key">None</span><span class="op">:</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t102" href="#t102">102</a></span><span class="t">        <span class="str">"""</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t103" href="#t103">103</a></span><span class="t"><span class="str">        Add a performance evaluation item to the performance_evaluation list.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t104" href="#t104">104</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t105" href="#t105">105</a></span><span class="t"><span class="str">        Args:</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t106" href="#t106">106</a></span><span class="t"><span class="str">            evaluation (str): The evaluation item to be added.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t107" href="#t107">107</a></span><span class="t"><span class="str">        """</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t108" href="#t108">108</a></span><span class="t">        <span class="nam">self</span><span class="op">.</span><span class="nam">performance_evaluation</span><span class="op">.</span><span class="nam">append</span><span class="op">(</span><span class="nam">evaluation</span><span class="op">)</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t109" href="#t109">109</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t110" href="#t110">110</a></span><span class="t">    <span class="key">def</span> <span class="nam">_generate_numbered_list</span><span class="op">(</span><span class="nam">self</span><span class="op">,</span> <span class="nam">items</span><span class="op">:</span> <span class="nam">List</span><span class="op">[</span><span class="nam">Any</span><span class="op">]</span><span class="op">,</span> <span class="nam">item_type</span><span class="op">=</span><span class="str">"list"</span><span class="op">)</span> <span class="op">-></span> <span class="nam">str</span><span class="op">:</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t111" href="#t111">111</a></span><span class="t">        <span class="str">"""</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t112" href="#t112">112</a></span><span class="t"><span class="str">        Generate a numbered list from given items based on the item_type.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t113" href="#t113">113</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t114" href="#t114">114</a></span><span class="t"><span class="str">        Args:</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t115" href="#t115">115</a></span><span class="t"><span class="str">            items (list): A list of items to be numbered.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t116" href="#t116">116</a></span><span class="t"><span class="str">            item_type (str, optional): The type of items in the list.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t117" href="#t117">117</a></span><span class="t"><span class="str">                Defaults to 'list'.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t118" href="#t118">118</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t119" href="#t119">119</a></span><span class="t"><span class="str">        Returns:</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t120" href="#t120">120</a></span><span class="t"><span class="str">            str: The formatted numbered list.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t121" href="#t121">121</a></span><span class="t"><span class="str">        """</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t122" href="#t122">122</a></span><span class="t">        <span class="key">if</span> <span class="nam">item_type</span> <span class="op">==</span> <span class="str">"command"</span><span class="op">:</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t123" href="#t123">123</a></span><span class="t">            <span class="nam">command_strings</span> <span class="op">=</span> <span class="op">[</span><span class="op">]</span>&nbsp;</span><span class="r"></span></p>
    <p class="par run show_par"><span class="n"><a id="t124" href="#t124">124</a></span><span class="t">            <span class="key">if</span> <span class="nam">self</span><span class="op">.</span><span class="nam">command_registry</span><span class="op">:</span>&nbsp;</span><span class="r"><span class="annotate short">124&#x202F;&#x219B;&#x202F;125</span><span class="annotate long">line 124 didn't jump to line 125, because the condition on line 124 was never true</span></span></p>
    <p class="mis show_mis"><span class="n"><a id="t125" href="#t125">125</a></span><span class="t">                <span class="nam">command_strings</span> <span class="op">+=</span> <span class="op">[</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t126" href="#t126">126</a></span><span class="t">                    <span class="nam">str</span><span class="op">(</span><span class="nam">item</span><span class="op">)</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t127" href="#t127">127</a></span><span class="t">                    <span class="key">for</span> <span class="nam">item</span> <span class="key">in</span> <span class="nam">self</span><span class="op">.</span><span class="nam">command_registry</span><span class="op">.</span><span class="nam">commands</span><span class="op">.</span><span class="nam">values</span><span class="op">(</span><span class="op">)</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t128" href="#t128">128</a></span><span class="t">                    <span class="key">if</span> <span class="nam">item</span><span class="op">.</span><span class="nam">enabled</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t129" href="#t129">129</a></span><span class="t">                <span class="op">]</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t130" href="#t130">130</a></span><span class="t">            <span class="com"># These are the commands that are added manually, do_nothing and terminate</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t131" href="#t131">131</a></span><span class="t">            <span class="nam">command_strings</span> <span class="op">+=</span> <span class="op">[</span><span class="nam">self</span><span class="op">.</span><span class="nam">_generate_command_string</span><span class="op">(</span><span class="nam">item</span><span class="op">)</span> <span class="key">for</span> <span class="nam">item</span> <span class="key">in</span> <span class="nam">items</span><span class="op">]</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t132" href="#t132">132</a></span><span class="t">            <span class="key">return</span> <span class="str">"\n"</span><span class="op">.</span><span class="nam">join</span><span class="op">(</span><span class="str">f"{i+1}. {item}"</span> <span class="key">for</span> <span class="nam">i</span><span class="op">,</span> <span class="nam">item</span> <span class="key">in</span> <span class="nam">enumerate</span><span class="op">(</span><span class="nam">command_strings</span><span class="op">)</span><span class="op">)</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t133" href="#t133">133</a></span><span class="t">        <span class="key">else</span><span class="op">:</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t134" href="#t134">134</a></span><span class="t">            <span class="key">return</span> <span class="str">"\n"</span><span class="op">.</span><span class="nam">join</span><span class="op">(</span><span class="str">f"{i+1}. {item}"</span> <span class="key">for</span> <span class="nam">i</span><span class="op">,</span> <span class="nam">item</span> <span class="key">in</span> <span class="nam">enumerate</span><span class="op">(</span><span class="nam">items</span><span class="op">)</span><span class="op">)</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t135" href="#t135">135</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t136" href="#t136">136</a></span><span class="t">    <span class="key">def</span> <span class="nam">generate_prompt_string</span><span class="op">(</span><span class="nam">self</span><span class="op">)</span> <span class="op">-></span> <span class="nam">str</span><span class="op">:</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t137" href="#t137">137</a></span><span class="t">        <span class="str">"""</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t138" href="#t138">138</a></span><span class="t"><span class="str">        Generate a prompt string based on the constraints, commands, resources,</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t139" href="#t139">139</a></span><span class="t"><span class="str">            and performance evaluations.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t140" href="#t140">140</a></span><span class="t">&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t141" href="#t141">141</a></span><span class="t"><span class="str">        Returns:</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t142" href="#t142">142</a></span><span class="t"><span class="str">            str: The generated prompt string.</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t143" href="#t143">143</a></span><span class="t"><span class="str">        """</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t144" href="#t144">144</a></span><span class="t">        <span class="nam">formatted_response_format</span> <span class="op">=</span> <span class="nam">json</span><span class="op">.</span><span class="nam">dumps</span><span class="op">(</span><span class="nam">self</span><span class="op">.</span><span class="nam">response_format</span><span class="op">,</span> <span class="nam">indent</span><span class="op">=</span><span class="num">4</span><span class="op">)</span>&nbsp;</span><span class="r"></span></p>
    <p class="run"><span class="n"><a id="t145" href="#t145">145</a></span><span class="t">        <span class="key">return</span> <span class="op">(</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t146" href="#t146">146</a></span><span class="t">            <span class="str">f"Constraints:\n{self._generate_numbered_list(self.constraints)}\n\n"</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t147" href="#t147">147</a></span><span class="t">            <span class="str">"Commands:\n"</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t148" href="#t148">148</a></span><span class="t">            <span class="str">f"{self._generate_numbered_list(self.commands, item_type='command')}\n\n"</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t149" href="#t149">149</a></span><span class="t">            <span class="str">f"Resources:\n{self._generate_numbered_list(self.resources)}\n\n"</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t150" href="#t150">150</a></span><span class="t">            <span class="str">"Performance Evaluation:\n"</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t151" href="#t151">151</a></span><span class="t">            <span class="str">f"{self._generate_numbered_list(self.performance_evaluation)}\n\n"</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t152" href="#t152">152</a></span><span class="t">            <span class="str">"You should only respond in JSON format as described below \nResponse"</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t153" href="#t153">153</a></span><span class="t">            <span class="str">f" Format: \n{formatted_response_format} \nEnsure the response can be"</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t154" href="#t154">154</a></span><span class="t">            <span class="str">"parsed by Python json.loads"</span>&nbsp;</span><span class="r"></span></p>
    <p class="pln"><span class="n"><a id="t155" href="#t155">155</a></span><span class="t">        <span class="op">)</span>&nbsp;</span><span class="r"></span></p>
</main>
<footer>
    <div class="content">
        <p>
            <a id="prevFileLink" class="nav" href="d_ed286290bb007969_text_py.html">&#xab; prev</a> &nbsp; &nbsp;
            <a id="indexLink" class="nav" href="index.html">&Hat; index</a> &nbsp; &nbsp;
            <a id="nextFileLink" class="nav" href="d_e1c04ba85fbf6b91_prompt_py.html">&#xbb; next</a>
            &nbsp; &nbsp; &nbsp;
            <a class="nav" href="https://coverage.readthedocs.io/en/7.2.3">coverage.py v7.2.3</a>,
            created at 2023-04-22 05:45 +0000
        </p>
    </div>
</footer>
</body>
</html>




print()