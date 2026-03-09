import sqlite3
import json

def migrate():
    try:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        
        # Get GameSection data with correct column names
        cursor.execute("SELECT id, id_name, emoji, title, description, tags, color_class, file_name, nav_label FROM core_gamesection")
        rows = cursor.fetchall()
        
        data = []
        for row in rows:
            data.append({
                "model": "core.gamesection",
                "pk": row[0],
                "fields": {
                    "id_name": row[1],
                    "emoji": row[2],
                    "title": row[3],
                    "description": row[4],
                    "tags": json.loads(row[5]) if isinstance(row[5], str) else row[5],
                    "color_class": row[6],
                    "file_name": row[7],
                    "nav_label": row[8]
                }
            })
            
        with open('data_juegos.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        print(f"Exportados {len(data)} juegos con éxito.")
        conn.close()
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Error: {e}")

if __name__ == "__main__":
    migrate()
