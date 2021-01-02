function output = my_predicter(images);
	
	classes = ["empty" "not_empty"];
	output = {};
	
	%change the path to Chess-piece-movement-tracker/final_model.onnx
	model_path = 'D:/Users/Phuntsho Wangdi/Desktop/Chess-piece-movement-tracker/final_model.onnx';
	
	model = importONNXNetwork(model_path,'OutputLayerType','classification','Classes',classes);

	%change this path to 'Chess-piece-movement-tracker/img/'
	D = 'D:/Users/Phuntsho Wangdi/Desktop/Chess-piece-movement-tracker/img/';
	S = dir(fullfile(D,'*.png'));
	N = natsortfiles({S.name});
	for k = 1:numel(N)
	    im_path = fullfile(D,N{k});
	    img = imread(im_path);
		prd = predict(model,img);
		output{k} = prd;
	end
end

