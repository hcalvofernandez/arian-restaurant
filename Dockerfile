FROM odoo:17.0
# Install Python dependencies
RUN pip3 install --no-cache-dir --break-system-packages python-escpos
# Expose necessary ports
EXPOSE 8069
# Run Odoo
CMD ["odoo"]