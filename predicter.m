function output = my_predicter(images);
	
	classes = ["empty" "not_empty"];
	output = {};
	model_path = 'D:/Users/Phuntsho Wangdi/Desktop/D/onnx/final_model.onnx';
	
	model = importONNXNetwork(model_path,'OutputLayerType','classification','Classes',classes);
	%imds = imageDatastore(images,'IncludeSubfolders',true,'LabelSource','foldernames');
	D = 'D:/Users/Phuntsho Wangdi/Desktop/D/UT/img/';
	S = dir(fullfile(D,'*.png'));
	N = natsortfiles({S.name});
	for k = 1:numel(N)
	    im_path = fullfile(D,N{k});
	    img = imread(im_path);
		prd = predict(model,img);
		output{k} = prd;
	end
end

