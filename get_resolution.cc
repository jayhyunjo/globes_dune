
void get_resolution(){
	ifstream fin("test3.dat");
	double x,y,chi;
	double x_tmp=300;
	vector<vector<double>> vec_tmp;
	vector<double> x_list;
	vector<double> y_list;
	TGraph *g1[1000];
	TGraph *g2[1000];
	double tmp_y=-180;
	int k=0;
	int i=0;
	vec_tmp.push_back(x_list);
	y_list.push_back(tmp_y);
	while(fin>>y>>x>>chi){
		if(y==tmp_y){
		 x_list.push_back(x);
		 vec_tmp[k].push_back(chi);	
		 i++;
	     cout<<"k= "<<k<<" i= "<<i<<" y= "<<y<<" x= "<<x<<" "<<chi<<endl;
		}else{
			g1[k] = new TGraph(int(i/2),&vec_tmp[k][0],&x_list[0]);
			g2[k] = new TGraph(i-i/2,&vec_tmp[k][int(i/2)],&x_list[int(i/2)]);
			tmp_y=y;
			k++;
			cout<<"k= "<<k<<" i= "<<i<<" y= "<<y<<" x= "<<x<<" new TGraph created "<<endl;
			y_list.push_back(tmp_y);
			vector<double> vec_new;
			x_list.clear();
			x_list.resize(0);
			vec_new.push_back(y);
			x_list.push_back(x);
			vec_tmp.push_back(vec_new);
		    i=1;	
		}
	}
			g1[k] = new TGraph(int(i/2),&vec_tmp[k][0],&x_list[0]);
			g2[k] = new TGraph(i-i/2,&vec_tmp[k][int(i/2)],&x_list[int(i/2)]);
			cout<<"k= "<<k<<" i= "<<i<<" new TGraph created "<<endl;
	vector<double> rec;
	for(int j=0;j<=k;j++){
		double x1 = g1[j]->Eval(1);
		double x2 = g2[j]->Eval(1);
		double resolution = fabs(x1-x2)/2;
		rec.push_back(resolution);
		cout<<y_list[j]<<"  "<<resolution<<endl;
	}
TGraph *g_res = new TGraph(k,&y_list[0],&rec[0]);
g_res->Draw();

}
