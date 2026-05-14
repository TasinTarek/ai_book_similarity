from odoo import models, fields, api, _
from odoo.addons.ai.orm.field_vector import Vector
from odoo.tools import SQL
import random

class AIExampleBook(models.Model):
    _name = 'ai.example.book'
    _description = 'AI Example Book'

    name = fields.Char("Title", required=True)
    description = fields.Text("Description")
    
    # Vector field (1536 dimensions for OpenAI compatibility)
    description_vector = Vector(size=1536)
    
    # Index for fast similarity search
    _description_vector_idx = models.Index("USING ivfflat (description_vector vector_cosine_ops)")

    def action_generate_mock_embedding(self):
        """Generates a random vector for demonstration purposes."""
        for record in self:
            # In a real scenario, you would call LLMApiService here
            mock_vector = [random.uniform(-1, 1) for _ in range(1536)]
            record.description_vector = mock_vector

    def action_find_similar(self):
        self.ensure_one()
        if not self.description_vector:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': _('No vector found'),
                    'message': _('Please generate a mock embedding first.'),
                    'type': 'warning',
                }
            }

        # Perform similarity search using the <=> operator
        # We search for the top 5 most similar books (excluding self)
        similar_ids = [id_ for id_, *_ in self.env.execute_query(SQL(
            """
            SELECT id
            FROM ai_example_book
            WHERE id != %s AND description_vector IS NOT NULL
            ORDER BY description_vector <=> %s::vector
            LIMIT 5
            """,
            self.id, self.description_vector
        ))]

        return {
            'name': _('Similar Books'),
            'type': 'ir.actions.act_window',
            'res_model': 'ai.example.book',
            'view_mode': 'list,form',
            'domain': [('id', 'in', similar_ids)],
            'target': 'new',
        }
