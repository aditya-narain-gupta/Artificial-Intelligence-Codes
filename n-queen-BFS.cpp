#include <bits/stdc++.h>
#define vt vector< vector<int> >
using namespace std ;

int n  ;
vector< vector< int > >mat(10,vector<int>(10)) ;
vector< vt >res ;

int isvalid( vt &state , int row , int col ){
//	cout<<row<<" "<<col<<"\n" ;
	for( int i = 0 ; i < col ; i++ ){
		if( state[row][i] == 1 ){
//			cout<<"bhak1\n";
			return 0 ;
		}
	}
	for( int i = row , j = col ; i >= 0 && j >= 0 ; i-- , j-- ){
		if( state[i][j] == 1 ){
//			cout<<"bhak2\n" ;
			return 0 ;
		}
	}
	for( int i = row , j = col ; i < n && j >= 0 ; i++ , j-- ){
		if( state[i][j] == 1 ){
//			cout<<"bhak3\n" ;
			return 0 ;
		}
	}
//	cout<<"bhak4\n" ;
	return 1 ;
}
int find_ans(){
	
	queue< pair< vt , int > >que ;
	map< vt , int >visited ;
	for( int i = 0 ; i < n ; i++ ){
		mat[i][0] = 1 ;
		que.push( make_pair( mat , 1 ) ) ;
		visited[ mat ] = 1 ;
		mat[i][0] = 0 ;
	}
	while( !que.empty() ){
		vt state = que.front().first ;
		int col = que.front().second ;
		que.pop() ;
		if( col >= n ){
			res.push_back( state ) ;
			continue ;
		}
	/*	for( int i = 0 ; i < n ; i++ ){
			for( int j = 0 ; j < n ; j++ ){
				cout<<state[i][j]<<" ";
			}
			cout<<"\n" ;
		}*/
		for( int i = 0 ; i < n ; i ++ ){
			if( isvalid(state,i,col) ){		
				state[i][col] = 1 ;
				if( visited.find(state) == visited.end() ){
					visited[state] = 1;
					que.push( make_pair(state,col+1) ) ;
				}
				state[i][col] = 0 ;
			}
		}
	}
	return 0 ;
}
int main(){
	cin>>n ;
	for( int i = 0 ; i < n ; i ++ ){
		for( int j = 0 ; j< n ; j ++ ){
			mat[i].push_back(0); 
		}
	}	
	find_ans() ;
	int sz = res.size() ;
	cout<<sz<<"\n" ;
	for( int k = 0 ; k < sz ; k++ ){
		vt ans = res[k] ;
		for( int i = 0 ; i < n ; i++ ){
			for( int j = 0 ; j < n ; j++ ){
				cout<<ans[i][j]<<" ";
			}
			cout<<"\n" ;
		}
		cout<<"\n" ;
	}
}
