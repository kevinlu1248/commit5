# commit-t5
Automatically generate commit messages locally. Currently using "SEBIS/code_trans_t5_small_commit_generation_transfer_learning_finetune", as it seems like the best quality for performance ratio (best T5-small model). Based on work of https://github.com/agemagician/CodeTrans, which uses data from https://github.com/epochx/commitgen.

FastT5 reduced the file sizes from 900mb (torch file) to a total of only 200mb (3 ONNX models) and the memory footprint to only 90mb. Further, the execution speed dropped from 1.3s to 0.5s.

```diff
diff --git a/README.md b/README.md
index 9b077d6..c9ee84c 100644
--- a/README.md
+++ b/README.md
@@ -6,7 +6,7 @@ React is a JavaScript library for building user interfaces.
 * **Efficient:** React minimizes interactions with the DOM by using a mock representation of the DOM.
 * **Flexible:** React works with the libraries and frameworks that you already know.
 
-[Learn how to use React in your own project.](http://facebook.github.io/docs/getting-started.html)
+[Learn how to use React in your own project.](http://facebook.github.io/react/docs/getting-started.html)
 
 ## Examples
 
@@ -41,7 +41,7 @@ The fastest way to get started is to serve JavaScript from the CDN:
 <script src="http://fb.me/JSXTransformer-0.3.0.js"></script>
 \`\`\`
 
-We've also built a [starter kit](#) which might be useful if this is your first time using React. It includes a webpage with an example of using React with live code.
+We've also built a [starter kit](http://facebook.github.io/react/downloads/react-0.3.0.zip) which might be useful if this is your first time using React. It includes a webpage with an example of using React with live code.
 
 If you'd like to use [bower](http://bower.io), it's as easy as:
```

### TODO
* Figure out how to load in 16-bit or 8-bit properly
* Turn into a Git tool
* Cleanup codebase
* Add a grammar checker 
* Fine-tune with all CommitGen data.

### Archive
ONNX Runtime improves performance from 1.3s to 670ms per iteration, but the resulting model is bigger (1.7gb of three files vs 800mb in original). Model can be found at https://huggingface.co/kevinlu1248/ct-base-commits-onnx/. Tests were conducted on the following example.

