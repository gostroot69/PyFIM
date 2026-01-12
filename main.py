import hashlib
import json
import os
import argparse
class Main:
    def __init__(self, file_path, type_hash):
        self.chunk_size = 4096
        self.hex_d = None
        self.file_path = file_path
        self.type_hash = type_hash

    def hash_file(self, json_path=None):
         try:
                res = {}
                hash_obj = hashlib.new(self.type_hash)
                file_key = os.path.basename(self.file_path)
                with open(self.file_path, 'rb') as f:
                    while True:
                        data = f.read(self.chunk_size)
                        if not data:
                            break    
                        hash_obj.update(data)
                self.hex_d = hash_obj.hexdigest()
                res[file_key] = self.hex_d
                try:
                        with open(json_path, 'w') as f:
                            json.dump(res, f, ensure_ascii=False, indent=4)
                            print(f"Hashes successfully added in {json_path}")
                except Exception as e:
                    print(f"Error {e}")
                return self.hex_d
         except Exception as e:
                return f"Error: {e}"
         
    def multi_hash_files(self, dir_path, json_path):
         try:
                res = {}
                for root, dirs, files in os.walk(dir_path):
                     for file in files:
                          hash_obj = hashlib.new(self.type_hash)
                          full_path = os.path.join(root, file)
                          file_key = os.path.relpath(full_path, dir_path)
                          with open(full_path, 'rb') as f:
                               while True:
                                    data = f.read(self.chunk_size)
                                    if not data:
                                         break
                                    hash_obj.update(data)
                          self.hex_d = hash_obj.hexdigest()
                          res[file_key] = self.hex_d
                try:
                        with open(json_path, 'w') as f:
                            json.dump(res, f, ensure_ascii=False, indent=4)
                            print(f"Hashes successfully added in {json_path}")
                except Exception as e:
                    print(f"Error {e}")
                return "All successfully added"
         except Exception as e:
                return f"Error: {e}"
    
    def date(self, file_name, json_path):
        try:
            res = {}
            if os.path.exists(json_path):
                with open(json_path, 'r') as f:
                    try:
                        res = json.load(f)
                    except json.JSONDecodeError:
                        res = {} 
            
            res[file_name] = self.hex_d
            
            with open(json_path, 'w') as f:
                json.dump(res, f, ensure_ascii=False, indent=4)
                return f"Hash successfully added in {json_path}"
        except Exception as e:
            return f"Error {e}"

    def check_hash(self, json_path, file_name):
         try:
              hash_obj = hashlib.new(self.type_hash)
              with open(self.file_path, 'rb') as f:
                    while True:
                        data = f.read(self.chunk_size)
                        if not data:
                            break    
                        hash_obj.update(data)
              current_hash = hash_obj.hexdigest()
              with open(json_path, 'r') as f:
                   res = json.load(f)
                   if res[file_name] == current_hash:
                        return f"File was checked and all right"
                   else:
                        return "Something went wrong"
         except Exception as e:
              return f"Error {e}"  
    def multi_check(self, json_path, dir_path):
        try:
                with open(json_path, 'r') as f:
                   res = json.load(f)
                for root, dirs, files in os.walk(dir_path):
                     for file in files:
                          hash_obj = hashlib.new(self.type_hash)
                          
                          full_path = os.path.join(root, file)
                          file_key = os.path.relpath(full_path, dir_path)
                          if file_key not in res:
                              print(f"Skipping {file_key}: not in JSON")
                              continue
                          with open(full_path, 'rb') as f:
                               while True:
                                    data = f.read(self.chunk_size)
                                    if not data:
                                         break
                                    hash_obj.update(data)
                          current_hash = hash_obj.hexdigest()
                          original_hash = res[file_key]
                          if original_hash == current_hash:
                               print(f"{file_key} is OK")
                          else:
                               print(f"Something went wrong with {file_key}")
                          
                return "Check was successfully"   
        except Exception as e:
                return f"Error {e}"
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FIM = File Integrity Monitor")
    
    parser.add_argument("-m", "--mode", choices=['hash_file', 'multi_hash', 'check_hash', 'multi_check'], 
                        help="Choose mode of operation", required=True)
    parser.add_argument("-f", "--file_path", help="Path to file (for hash_file or check_hash)")
    parser.add_argument("-t", "--type", default="sha256", help="Type hash (for example, sha256, md5)")
    parser.add_argument("-json", "--json_path", help="Path to JSON datebase")
    parser.add_argument("-d", "--dir_path", help="Path to directory (for multi_hash or multi_check)")
    parser.add_argument("-n", "--name", help="Name key (file_name) for JSON")
    
    args = parser.parse_args()

    app = Main(args.file_path, args.type)

    try:
        if args.mode == 'hash_file':
            if not args.file_path:
                print("Error: write -f (file_path)")
            else:
                print(f"File hash: {app.hash_file(args.json_path)}")

        elif args.mode == 'multi_hash':
            if not args.dir_path or not args.json_path:
                print("Error: write -d (dir_path) and -json (json_path)")
            else:
                print(app.multi_hash_files(args.dir_path, args.json_path))

        elif args.mode == 'check_hash':
            if not args.json_path or not args.name or not args.file_path:
                print("Error: write -json, -f and -n (name in base)")
            else:
                print(app.check_hash(args.json_path, args.name))

        elif args.mode == 'multi_check':
            if not args.json_path or not args.dir_path:
                print("Error: write -json and -d (dir_path)")
            else:
                print(app.multi_check(args.json_path, args.dir_path))

    except Exception as e:
        print(f"Something went wrong, error: {e}")
