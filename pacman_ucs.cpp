#include<bits/stdc++.h>
#define vt vector< vector<int> >
using namespace std ;
int n , m ;
int pr,pc,fr,fc ;
vector< vector<int> >mat(100,vector<int>(100)) ;
vector< vector<int> >dist(100,vector<int>(100)) ;
map< vt , vt >map1 ;
map< pair<int,int> , pair<int,int> >parent ;

int dx[] = {-1,1,0,0} ;
int dy[] = {0,0,-1,1} ;
queue< pair<int,int> >que ;
int find_ans(){
	
	que.push( make_pair(pr,pc) ) ;
	dist[pr][pc] = 0 ;
	parent[make_pair(pr,pc)] = make_pair(pr,pc) ;
	
	while( !que.empty() ){
		int x = que.front().first ;
		int y = que.front().second ;
	//	cout<<x<<" "<<y<<"\n" ;
		que.pop() ;
		
		if( x == fr && y == fc ){	
			cout<<"aish\n" ;
		}
		else{
			for( int i = 0 ; i < 4 ; i++ ){
				int u = x + dx[i] ;
				int v = y + dy[i]  ;
				if( u >= 0 && u < n && v >= 0 && v < m && mat[u][v] != 0 ){
					if( dist[u][v] > dist[x][y] + 1 ){
						dist[u][v] = dist[x][y] + 1 ;
						parent[make_pair(u,v)] = make_pair(x,y) ;
						que.push( make_pair(u,v)) ;
					}
				}
			}
		}
	}
}

int main(){
	cin>>pr>>pc ; 
	cin>>fr>>fc ;
	cin>>n>>m ;
	for( int i = 0 ; i < n ; i++ ){
		for( int j = 0 ; j < m ; j++ ){
			char ch ;
			int x ;
			cin>>ch ;
			if( ch == '%' ){
				x = 0 ;
			}
			else if( ch == '-' ){
				x = 1 ;
			}
			else if( ch == 'P' ){
				x = 2 ;
			}
			else{
				x = 3 ; 
			}
			mat[i][j] = x ;
			dist[i][j] = 9999999;
		}
	}
	
	find_ans() ;
	if( dist[fr][fc] >= 9999999 ){
		cout<<"NOT POSSIBLE\n" ;
	}
	else{
		cout<<dist[fr][fc]<<"\n" ;
		vector< pair<int,int> >vec ;
		int x = fr ;
		int y = fc ;
		vec.push_back( make_pair(x,y) ) ;
		while(1){
			int px = parent[make_pair(x,y)].first ;
			int py = parent[make_pair(x,y)].second ;
			if( x == px && y == py ){
				break ;
			}
			vec.push_back( make_pair(px,py) ) ;
			x = px ;
			y = py ;
			
		}
		reverse( vec.begin() , vec.end() ) ;
		for( int i = 0 ; i < vec.size() ; i++ ){
			cout<<vec[i].first<<" "<<vec[i].second<<"\n";
		}
	}
	
}
