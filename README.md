# commit5
Automatically generate commit messages locally using T5. Currently using "SEBIS/code_trans_t5_small_commit_generation_transfer_learning_finetune", as it seems like the best quality for performance ratio (best T5-base model). Based on work of https://github.com/agemagician/CodeTrans, which uses data from https://github.com/epochx/commitgen.

FastT5 reduced the file sizes from 900mb (torch file) to a total of only 200mb (3 ONNX models) and the memory footprint to only 90mb. Further, the execution speed dropped from 1.3s to 0.5s.

```diff
diff --git a/grunt/tasks/release.js b/grunt/tasks/release.js
index efbb2e7..d377ee4 100644
--- a/grunt/tasks/release.js
+++ b/grunt/tasks/release.js
@@ -7,7 +7,7 @@ var grunt = require('grunt');
 
 var BOWER_PATH = '../react-bower/';
 var BOWER_GLOB = [BOWER_PATH + '*'];
-var BOWER_FILES = ['React.js', 'React.min.js', 'JSXTransformer.js'];
+var BOWER_FILES = ['react.js', 'react.min.js', 'JSXTransformer.js'];
 var GH_PAGES_PATH = '../react-gh-pages/';
 var GH_PAGES_GLOB = [GH_PAGES_PATH + '*'];
```

### Vision
I think in general there's a huge space for locally running LM-based devtools. There's generally huge privacy concerns in corporations around productivity tools for dev which is the problem around adoptivity of tools like Copilot/Codeium/Tabnine in companies, and I think powerful LM's can be built smaller while laptops are becoming beefier. There's also an assortment of optimizations (distillation + ONNX + quantization + llama.cpp) for running LLM's on lower-power machines.

### Archive
ONNX Runtime improves performance from 1.3s to 670ms per iteration, but the resulting model is bigger (1.7gb of three files vs 800mb in original). Model can be found at https://huggingface.co/kevinlu1248/ct-base-commits-onnx/. Tests were conducted on the following example.

### TODO
- [x] Figure out how to load in 16-bit or 8-bit properly
- [x] Turn into a Git tool
- [x] Cleanup codebase
- [ ] Upload to pypa
- [ ] Migrate to CodeTrans-small
- [ ] Add a grammar checker 
- [ ] Use CodeT5+
