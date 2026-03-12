#import dns.resolver

# Pydroid 3 အတွက် DNS ဖြေရှင်းချက်
#dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
#dns.resolver.default_resolver.nameservers = ['8.8.8.8', '8.8.4.4', '1.1.1.1']

from motor.motor_asyncio import AsyncIOMotorClient
from pyrogram import filters
from maythusharmusic import app
from config import OWNER_ID

@app.on_message(filters.command("migrate") & filters.user(OWNER_ID))
async def migrate_db_command(client, message):
    await message.reply_text("🔄 Database ကူးယူခြင်း စတင်ပါပြီ... ခေတ္တစောင့်ပါ။")
    
    try:
        # သင့်ရဲ့ URI များကို ဒီနေရာမှာ ပြင်ထည့်ပါ
        source_uri = "mongodb+srv://pyaesone:pyaesone@pyaesone.ii8wsxo.mongodb.net/?retryWrites=true&w=majority"
        dest_uri = "mongodb+srv://Bby_nnds_db_user:bbynnds@bbynnds.tnixpfw.mongodb.net/?appName=bbynnds"
        
        source_client = AsyncIOMotorClient(source_uri)
        dest_client = AsyncIOMotorClient(dest_uri)
        
        source_db = source_client["maythusharmusic"]
        dest_db = dest_client["maythusharmusic"]
        
        collections_to_migrate = [
            "adminauth", "authuser", "autoend", "assistants", "blacklistChat", 
            "blockedusers", "chats", "cplaymode", "upcount", "gban", "language", 
            "onoffper", "playmode", "playtypedb", "skipmode", "sudoers", 
            "tgusersdb", "privatechats", "suggestion", "cleanmode", "queries", 
            "userstats", "vipvideocalls", "chatsc", "tgusersdbc", "ytcache", 
            "songfiles", "couple", "afk", "nightmode", "notes", "filters"
        ]
        
        status_msg = await message.reply_text("စတင်ဖတ်ရှုနေပါသည်...")
        success_count = 0
        
        for col_name in collections_to_migrate:
            source_collection = source_db[col_name]
            dest_collection = dest_db[col_name]
            
            # Source မှ data များကို ယူခြင်း
            cursor = source_collection.find({})
            data_list = await cursor.to_list(length=None)
            
            if data_list:
                # Destination သို့ ထည့်သွင်းခြင်း
                await dest_collection.insert_many(data_list)
                success_count += 1
                await status_msg.edit_text(f"✅ `{col_name}` မှ data ({len(data_list)}) ခု ကူးယူပြီးပါပြီ။")
        
        await message.reply_text(f"🎉 Database ကူးယူခြင်း ပြီးဆုံးပါပြီ။ Collection ပေါင်း ({success_count}) ခုကို အောင်မြင်စွာ ကူးယူနိုင်ခဲ့ပါသည်။")
        
    except Exception as e:
        await message.reply_text(f"❌ အမှားဖြစ်ပေါ်ခဲ့သည်: {e}")
