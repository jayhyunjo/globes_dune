void plot(){
	TGraph *g[5];
	int color[] = {kOrange, kGreen, kRed,kBlack ,kBlue};
	for(int i=0;i<1;i++){
		if(i==3)continue;
		//g[i] = new TGraph(Form("dune_%i.dat",i));
		g[i] = new TGraph("dune_dcp_ori.dat");
		g[i] ->SetLineWidth(2);
		g[i]->SetLineColor(color[i]);
		if(i==0)g[i]->Draw();
		else g[i]->Draw("same");
	}
	g[0]->GetYaxis()->SetRangeUser(0,10);
}
