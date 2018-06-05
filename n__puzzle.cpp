/// <-----------------Aishwarya Dutt Maurya -------->
#include<bits/stdc++.h>
#define vt vector< vector<int> >
using namespace std ;
int n ;

map< vt , vt >parent ;
vector< vector<int> >mat(10,vector<int>(10)) ;
vector< vector<int> >goal(10,vector<int>(10)) ;
int dx[] = {-1,0,1,0} ;
int dy[] = {0,-1,0,1} ;

int isgoalfound( vt state ){
	
	for( int i = 0 ; i < n ; i++ ){
		for( int j = 0 ; j < n ; j++ ){
			if( state[i][j] != goal[i][j] ){
				return false; 
			}
		}
	}
	return true ;
}

int printstate( vt state ){
	for( int i = 0 ; i < n ;i++ ){
		for( int j = 0 ; j < n ; j++ ){
			cout<<state[i][j]<<" ";
		}
		cout<<"\n" ;
	}
	cout<<"<------------------------------------>\n" ;
}
void find_ans( int u , int v ){
	
	queue< pair< vt , pair<int,int> > >que;
	que.push(make_pair(mat,make_pair(u,v))) ;
	map< vt , int >visited; 
	parent[mat] = mat ;
	visited[mat] = 1 ;
	while( !que.empty() ){
		vt state = que.front().first ;
		u = que.front().second.first ;
		v = que.front().second.second ;
		que.pop() ;
		vt par = state ;
		if( isgoalfound( state ) ){
	//		cout<<"aihd\n" ;
			return ;
		}
		for( int i = 0 ; i < 4 ; i++ ){
			int x = u + dx[i] ;
			int y = v + dy[i] ;
			if( x >= 0 && x < n && y >= 0 && y < n ){
				int temp = state[x][y] ;
				state[x][y] = state[u][v] ;
				state[u][v] = temp ;
				if( visited.find(state) == visited.end() ){
					visited[state] = 1 ;
					parent[state] = par ;
					que.push( make_pair(state,make_pair(x,y))) ;
				}
				temp = state[x][y] ;
				state[x][y] = state[u][v] ;
				state[u][v] = temp ;
			}
		}
	}	
}

int main(){
	
	cin>>n ;
	int u,v ;
	for( int i = 0 ; i < n ; i++ ){
		for( int j = 0 ; j < n ; j++ ){
			int x ;
			cin>>x ;
			if( x == 0 ){
				u = i ,v = j ;
			}
			mat[i][j] = x ;
		}
	}
	int val = 0 ;
	for( int i = 0 ; i < n ; i++ ){
		for( int j = 0 ; j < n ; j++ ){
			goal[i][j] = val++ ; 
		}
	}
/*	for( int i = 0 ; i < n ; i++ ){
		for( int j = 0 ; j < n ; j++ ){
			cout<<goal[i][j]<<" ";
		}
		cout<<"\n" ;
	}*/
	find_ans(u,v) ;
	vt state = goal ;
	vector< vt >res ;
	res.push_back(goal) ;
	while( parent[state] != state ){
		res.push_back(state) ;
		state = parent[state] ;
	} 
	int sz = res.size()  ;
	cout<<sz<<"\n" ;
	res.push_back( parent[state] ) ;
	reverse( res.begin() , res.end() ) ;
	for( int i = 0 ; i < sz ; i++ ){
		state = res[i] ;
		printstate(state) ;
	}
	
}
