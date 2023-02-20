#include <iostream>
#include <string>
using namespace std;

class bin_fid_num {
	int n;
	int m;
	string a;
	string b;

	public:
		bin_fid_num(int n, int m, string a, string b) {
			this->n = n;
			this->m = m;
			this->a = a;
			this->b = b;
			
		}
		void find() {
			for (int i = 0; i < m+(m-1); i++) {
				int y_n=a.find(b[i]);
				if (b[i] == ' ');
				else if (y_n == -1) {
					cout << 0 << endl;
				}
				else
					cout << 1 << endl;

			}
				
		}
};

int main() {
	int n;
	cin >> n;
	cin.ignore();
	string a;
	getline(cin, a);

	int m;
	cin >> m;
	cin.ignore();
	string b;
	getline(cin, b);

	bin_fid_num bfn(n, m, a, b);
	bfn.find();

	
	return 0;

}